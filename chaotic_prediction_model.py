import tensorflow as tf
from tensorflow.contrib import slim
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

def oscillator(I, u, v, z):
    a1, a2, a3, a4 = 0.6, 0.6, -0.5, 0.5
    b1, b2, b3, b4 = -0.6, -0.6, -0.5, 0.5
    k = 50
    u_v = tf.nn.tanh(a1*u + a2*v - a3*z + a4*I)
    v_v = tf.nn.tanh(b1*z - b2*u - b3*v + b4*I)
    w = tf.nn.tanh(I)
    z_v = ( v_v - u_v )* tf.exp(-k*I*I)+ w
    return u_v, v_v, z_v

def weight_variable(shape):
    initial = tf.contrib.layers.xavier_initializer()
    return tf.Variable(initial(shape))

def bias_variable(shape):
    initial = tf.contrib.layers.xavier_initializer()
    return tf.Variable(initial(shape))

def read_csv(file):
    result = []
    current_day = []
    data = np.genfromtxt(file, delimiter=",",skip_header=1)
    data = data[:,[3,4,5,6,8]]
    data, norms = normalize(data, axis=0, norm='l2',return_norm=True)

    current_day.append(data[:length_of_training_records-1])
    current_day = np.array(current_day)

    for i in range(length_of_training_records,len(data)):
        result.append(data[i-length_of_training_records:i])
    result = np.array(result)
    np.random.shuffle(result)
    tr_set = result[:int(0.8*len(result))]
    te_set = result[int(0.8*len(result)):]
    return tr_set, te_set, current_day, norms

def read_lastest_indicator():
    result= []
    return 0

#hyper parameter
epoch = 1200
length_of_training_records = 10
training_rate = 1e-5

#IO
# data_add ="C:\\Users\\willh\\AppData\\Roaming\\MetaQuotes\\Terminal\\Common\\Files\\Project_Data\\"
data_add ="C:\\Users\\UIC\\Downloads\\"
# list file in directory
file_names = [] 
for root, dirs, files in os.walk(data_add):
    for file in files:
        if ('.csv') in file:
            file_names.append(data_add+file)

# network strcture
ph_input_vector = tf.placeholder(tf.float32,[None, 5,1])
ph_label_vector = tf.placeholder(tf.float32,[1,5])

ph_u_1,ph_u_2,ph_u_3= tf.placeholder(tf.float32,[1,None]),tf.placeholder(tf.float32,[1,None]),tf.placeholder(tf.float32,[1,None])
ph_v_1,ph_v_2,ph_v_3=tf.placeholder(tf.float32,[1,None]),tf.placeholder(tf.float32,[1,None]),tf.placeholder(tf.float32,[1,None])
ph_z_1,ph_z_2,ph_z_3=tf.placeholder(tf.float32,[1,None]),tf.placeholder(tf.float32,[1,None]),tf.placeholder(tf.float32,[1,None])



cell = tf.nn.rnn_cell.GRUCell(num_units = 1)
init_state = cell.zero_state(batch_size=5,dtype = tf.float32)#batch size intented to be, out can be [-1, 1100] multiply oneby one
GRU_outputs, final_state = tf.nn.dynamic_rnn(cell, ph_input_vector, initial_state=init_state, time_major=True)

#fully connect layer
W_fc_1 = weight_variable([5, 20])
b_fc_1 = bias_variable([20])
ph_u_1,ph_v_1,h_fc_1 = oscillator(tf.matmul(tf.transpose(final_state),W_fc_1)+b_fc_1,ph_u_1,ph_v_1,ph_z_1)
# h_fc_1 = tf.nn.leaky_relu(tf.matmul(tf.transpose(final_state),W_fc_1)+b_fc_1)

W_fc_2 = weight_variable([20, 30])
b_fc_2 = bias_variable([30])
ph_u_2,ph_v_2,h_fc_2 = oscillator(tf.matmul(h_fc_1,W_fc_2)+b_fc_2,ph_u_2,ph_v_2,ph_z_2)
# h_fc_2 = tf.nn.leaky_relu(tf.matmul(h_fc_1,W_fc_2)+b_fc_2)

W_fc_3 = weight_variable([30, 5])
b_fc_3 = bias_variable([5])
ph_u_3,ph_v_3,h_fc_3 = oscillator(tf.matmul(h_fc_2,W_fc_3)+b_fc_3,ph_u_3,ph_v_3,ph_z_3)
# h_fc_3 = tf.nn.leaky_relu(tf.matmul(h_fc_2,W_fc_3)+b_fc_3)


#evaluate and optimization
MSE = tf.reduce_mean((ph_label_vector- h_fc_3)**2)
# MSE,_= tf.metrics.mean_squared_error(ph_label_vector, final_state)
train_step = tf.train.AdamOptimizer(training_rate).minimize(MSE)

with tf.Session() as sess:
    #input from every single csv to form tranning data
    for file in file_names: #for every single product
        print("for product "+str(file))
        training_set, testing_set, latest_day, norms = read_csv(file)

        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
###############
        # continue
###############
        #train network
        for i in range(0,epoch):
            count = 0
            loss = np.zeros(len(training_set))
            for record in training_set:
                input_vector = np.reshape(record[:length_of_training_records-1], (length_of_training_records-1,-1,1))
                label_vector = record[length_of_training_records-1:]

                _, l, prediction = sess.run([train_step,MSE,h_fc_3], feed_dict = {
                    ph_input_vector:input_vector,
                    ph_label_vector:label_vector
                    })
                loss[count] = l
                count += 1
            print("epoch No."+str(i)+ " avrage loss: "+str(np.mean(loss))+" std "+str(np.std(loss)))

        #test
        count = 0
        loss = np.zeros(len(testing_set))
        for record in testing_set:
            input_vector = np.reshape(record[:length_of_training_records-1], (length_of_training_records-1,-1,1))
            label_vector = record[length_of_training_records-1:]

            _, l, prediction = sess.run([train_step,MSE,h_fc_3], feed_dict = {
                ph_input_vector:input_vector,
                ph_label_vector:label_vector
                })
            loss[count] = l
            count += 1
        print("Test finished "+ " avrage loss: "+str(np.mean(loss))+" std "+str(np.std(loss)))

        # predict tomorrow's indicators
        input_vector = np.reshape(latest_day, (length_of_training_records-1,-1,1))
        prediction = sess.run(h_fc_3, feed_dict = {
        ph_input_vector:input_vector        })

        prediction = np.asarray(prediction)
        prediction = prediction*norms
        print("for product "+str(file))
        print("for tomorrow's indicator "+str(prediction))
        print("     ")