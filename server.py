# Imports
#test
from math import floor
import socket
import select
import threading
import random
import datetime
from cryptography.fernet import Fernet
import os
import pickle

# Initialize global variables
HEADER = 128
MAX_PACKAGE_LENGTH = 128
PORT = 5050
DATETIMEFORMAT = "%d/%m/%Y %H:%M:%S"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = b''

# Upper and lower rejection limits for HTZ products
LOWER_REJ_HTZ_1 = 22
LOWER_TOL_HTZ_1 = 23
UPPER_TOL_HTZ_1 = 25
UPPER_REJ_HTZ_1 = 26
LOWER_REJ_HTZ_3 = 22
LOWER_TOL_HTZ_3 = 23
UPPER_TOL_HTZ_3 = 25
UPPER_REJ_HTZ_3 = 26
LOWER_REJ_HTZ_31 = 22
LOWER_TOL_HTZ_31 = 23
UPPER_TOL_HTZ_31 = 25
UPPER_REJ_HTZ_31 = 26
LOWER_REJ_HTZ_5 = 22
LOWER_TOL_HTZ_5 = 23
UPPER_TOL_HTZ_5 = 25
UPPER_REJ_HTZ_5 = 26
LOWER_REJ_HTZ_51 = 22
LOWER_TOL_HTZ_51 = 23
UPPER_TOL_HTZ_51 = 25
UPPER_REJ_HTZ_51 = 26

# Load trained ML models for PV prediction (ONLY LOAD BEST PERFORMING MODEL FOR EACH HTZ PRODUCT)

'''
# sklearn LinearRegression
with open('ml models/HTZ_1_lightGBM.pkl', 'rb') as f:
    lr_HTZ_1, score_lr_HTZ_1 = pickle.load(f)
    print("lr_HTZ_3 score:", score_lr_HTZ_1)  
with open('ml models/HTZ_3_lr.pkl', 'rb') as f:
    lr_HTZ_3, score_lr_HTZ_3 = pickle.load(f)
    print("lr_HTZ_3 score:", score_lr_HTZ_3)  
with open('ml models/HTZ_31_lr.pkl', 'rb') as f:
    lr_HTZ_31, score_lr_HTZ_31 = pickle.load(f)
    print("lr_HTZ_31 score:", score_lr_HTZ_31)
with open('ml models/HTZ_5_lr.pkl', 'rb') as f:
    lr_HTZ_5, score_lr_HTZ_5 = pickle.load(f)
    print("lr_HTZ_5 score:", score_lr_HTZ_5)
with open('ml models/HTZ_51_lr.pkl', 'rb') as f:
    lr_HTZ_51, score_lr_HTZ_51 = pickle.load(f)
    print("lr_HTZ_51 score:", score_lr_HTZ_51)

# sklearn PolynomialRegression
with open('ml models/HTZ_1_pr.pkl', 'rb') as f:
    pr_HTZ_1, degree_pr_HTZ_1, score_pr_HTZ_1 = pickle.load(f)
    print("score_pr_HTZ_1:", score_pr_HTZ_1)
with open('ml models/HTZ_3_pr.pkl', 'rb') as f:
    pr_HTZ_3, degree_pr_HTZ_3, score_pr_HTZ_3 = pickle.load(f)
    print("score_pr_HTZ_3:", score_pr_HTZ_3)
with open('ml models/HTZ_31_pr.pkl', 'rb') as f:
    pr_HTZ_31, degree_pr_HTZ_31, score_pr_HTZ_31 = pickle.load(f)
    print("score_pr_HTZ_31:", score_pr_HTZ_31)
with open('ml models/HTZ_5_pr.pkl', 'rb') as f:
    pr_HTZ_5, degree_pr_HTZ_5, score_pr_HTZ_5 = pickle.load(f)
    print("score_pr_HTZ_5:", score_pr_HTZ_5)
with open('ml models/HTZ_51_pr.pkl', 'rb') as f:
    pr_HTZ_51, degree_pr_HTZ_51, score_pr_HTZ_51 = pickle.load(f)
    print("score_pr_HTZ_51:", score_pr_HTZ_51)

# lightGBM
with open('ml models/HTZ_1_lightGBM.pkl', 'rb') as f:
    gbm_HTZ_1, r2_HTZ_1, rmse_HTZ_1 = pickle.load(f)
    print("gbm_HTZ_1 r2 score:", r2_HTZ_1)
    print("gbm_HTZ_1 rmse:", rmse_HTZ_1)
with open('ml models/HTZ_3_lightGBM.pkl', 'rb') as f:
    gbm_HTZ_3, r2_HTZ_3, rmse_HTZ_3 = pickle.load(f)
    print("gbm_HTZ_3 r2 score:", r2_HTZ_3)
    print("gbm_HTZ_3 rmse:", rmse_HTZ_3)
with open('ml models/HTZ_31_lightGBM.pkl', 'rb') as f:
    gbm_HTZ_31, r2_HTZ_31, rmse_HTZ_31 = pickle.load(f)
    print("gbm_HTZ_31 r2 score:", r2_HTZ_31)
    print("gbm_HTZ_31 rmse:", rmse_HTZ_31)
with open('ml models/HTZ_5_lightGBM.pkl', 'rb') as f:
    gbm_HTZ_5, r2_HTZ_5, rmse_HTZ_5 = pickle.load(f)
    print("gbm_HTZ_5 r2 score:", r2_HTZ_5)
    print("gbm_HTZ_5 rmse:", rmse_HTZ_5)
with open('ml models/HTZ_51_lightGBM.pkl', 'rb') as f:
    gbm_HTZ_51, r2_HTZ_51, rmse_HTZ_51 = pickle.load(f)
    print("gbm_HTZ_51 r2 score:", r2_HTZ_51)
    print("gbm_HTZ_51 rmse:", rmse_HTZ_51)

# XGBoost
with open('ml models/HTZ_1_XGBoost.pkl', 'rb') as f:
    xgb_HTZ_1, r2_xgb_HTZ_1, rmse_xgb_HTZ_1 = pickle.load(f)
    print("xgb_HTZ_1 r2 score:", r2_xgb_HTZ_1)
    print("xgb_HTZ_1 rmse:", rmse_xgb_HTZ_1)

with open('ml models/HTZ_3_XGBoost.pkl', 'rb') as f:
    xgb_HTZ_3, r2_xgb_HTZ_3, rmse_xgb_HTZ_3 = pickle.load(f)
    print("xgb_HTZ_3 r2 score:", r2_xgb_HTZ_3)
    print("xgb_HTZ_3 rmse:", rmse_xgb_HTZ_3)
    
with open('ml models/HTZ_31_XGBoost.pkl', 'rb') as f:
    xgb_HTZ_31, r2_xgb_HTZ_31, rmse_xgb_HTZ_31 = pickle.load(f)
    print("xgb_HTZ_31 r2 score:", r2_xgb_HTZ_31)
    print("xgb_HTZ_31 rmse:", rmse_xgb_HTZ_31)
    
with open('ml models/HTZ_5_XGBoost.pkl', 'rb') as f:
    xgb_HTZ_5, r2_xgb_HTZ_5, rmse_xgb_HTZ_5 = pickle.load(f)
    print("xgb_HTZ_5 r2 score:", r2_xgb_HTZ_5)
    print("xgb_HTZ_5 rmse:", rmse_xgb_HTZ_5)
    
with open('ml models/HTZ_51_XGBoost.pkl', 'rb') as f:
    xgb_HTZ_51, r2_xgb_HTZ_51, rmse_xgb_HTZ_51 = pickle.load(f)
    print("xgb_HTZ_51 r2 score:", r2_xgb_HTZ_51)
    print("xgb_HTZ_51 rmse:", rmse_xgb_HTZ_51)

# AdaBoost
with open('ml models/HTZ_1_AdaBoost.pkl', 'rb') as f:
    ABR_HTZ_1, r2_ABR_HTZ_1, rmse_ABR_HTZ_1 = pickle.load(f)
    print("ABR_HTZ_1 r2 score:", r2_ABR_HTZ_1)
    print("ABR_HTZ_1 rmse:", rmse_ABR_HTZ_1)

with open('ml models/HTZ_3_AdaBoost.pkl', 'rb') as f:
    ABR_HTZ_3, r2_ABR_HTZ_3, rmse_ABR_HTZ_3 = pickle.load(f)
    print("ABR_HTZ_3 r2 score:", r2_ABR_HTZ_3)
    print("ABR_HTZ_3 rmse:", rmse_ABR_HTZ_3)
    
with open('ml models/HTZ_31_AdaBoost.pkl', 'rb') as f:
    ABR_HTZ_31, r2_ABR_HTZ_31, rmse_ABR_HTZ_31 = pickle.load(f)
    print("ABR_HTZ_31 r2 score:", r2_ABR_HTZ_31)
    print("ABR_HTZ_31 rmse:", rmse_ABR_HTZ_31)
    
with open('ml models/HTZ_5_AdaBoost.pkl', 'rb') as f:
    ABR_HTZ_5, r2_ABR_HTZ_5, rmse_ABR_HTZ_5 = pickle.load(f)
    print("ABR_HTZ_5 r2 score:", r2_ABR_HTZ_5)
    print("ABR_HTZ_5 rmse:", rmse_ABR_HTZ_5)
    
with open('ml models/HTZ_51_AdaBoost.pkl', 'rb') as f:
    ABR_HTZ_51, r2_ABR_HTZ_51, rmse_ABR_HTZ_51 = pickle.load(f)
    print("ABR_HTZ_51 r2 score:", r2_ABR_HTZ_51)
    print("ABR_HTZ_51 rmse:", rmse_ABR_HTZ_51)
'''

# Boundary colors
RED_BOUND_COL = "FF0000"
ORANGE_BOUND_COL = "FFA500"

# List for HTZ porevolumes
HTZ_PV = ['HTZ-1 porevolume', 'HTZ-3 porevolume',
          'HTZ-31 porevolume', 'HTZ-5 porevolume', 'HTZ-51 porevolume']

# Encryption/decryption key
#key = Fernet.generate_key()

# Save key to dedicated file
# Open the file as wb to write bytes
#file = open(os.getenv('LOCALAPPDATA') + 'key.key', 'wb')
# file.write(key)  # The key is type bytes still
# file.close()
# print(key)

# Read encryption keys from dedicated file
# file = open('keys.key', 'rb')  # Open the file as wb to read bytes
# key = file.read()  # The key will be type bytes
# file.close()

"""
# List of tag numbers for HTZ porevolume analysis
TAGNRS = ["820_WQT_110", "820_WQT_120", "820_WQT_130", "820_WQT_140", "820_WQT_100", "820_STDEV_WIC_110", "820_STDEV_WIC_120",
          "820_STDEV_WIC_130", "820_STDEV_WIC_140", "820_STDEV_WIC_100", "820_WQT_160", "820_STDEV_WIC_160", "820_FT_170",
          "820_FT_171", "820_HIC_170", "820_XT_170", "820_N_160", "820_HIC_175", "820_XT_175", "820_PT_175", "820_TT_175",
          "820_HIC_176", "820_PT_310", "820_TT_311A", "820_TT_312A", "820_TT_313A", "820_TT_314A", "820_TT_315A", "820_TT_316A",
          "820_TT_311B", "820_TT_312B", "820_TT_313B", "820_TT_314B", "820_TT_315B", "820_TT_316B", "820_HIC_317", "820_HIC_310B",
          "820_TT_318", "820_FT_310", "820_TT_317"]
"""

# Instantiate server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Instantiate encryptor/decryptor
#encryptor = Fernet(key)

# Thread function to handle client connections


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            ready_to_read, ready_to_write, in_error = \
                select.select([conn, ], [conn, ], [], 5)
        except:
            print(f"[NEW DISCONNECTION] {addr} disconnected.")
            break

        if ready_to_read:
            # Receive message from client
            try:
                msg_length = conn.recv(HEADER)
            except:
                print(f"[NEW DISCONNECTION] {addr} disconnected.")
                conn.close()
                return

            if (msg_length == DISCONNECT_MESSAGE):
                print(f"[NEW DISCONNECTION] {addr} disconnected.")
                conn.close()
                return

            if len(msg_length) != 0:
                msg_length = int(msg_length.decode(FORMAT).strip("\x00"))
                msg = conn.recv(msg_length).decode(FORMAT)

            if ready_to_write:
                # Send message to client
                send_data(handle_request(msg), conn)

    # Close connection
    conn.close()


def send_data(response, conn):
    # Encode
    response = response.encode(FORMAT)
    # Create a header for the first 128 bytes
    # This header is received first on the client
    # It tells the client how big the message is
    header = str(len(response))
    header = header.encode(FORMAT)
    buffer = "\x00"*(HEADER-len(header))
    buffer = buffer.encode(FORMAT)
    header += buffer
    # Add the header in front of the response
    response = header + response

    # We have to do this workaround since sending one big package doesn't work
    currentPackageOffset = 0
    while currentPackageOffset < len(response):
        # Send a partial message.
        # (Visual code auto formats like this. Yikes...)
        sendLength = min(MAX_PACKAGE_LENGTH, len(
            response) - currentPackageOffset)
        conn.send(
            response[currentPackageOffset:currentPackageOffset + sendLength])
        currentPackageOffset += sendLength


# Data format is as follows
# N:TagNr,T:Time,V:value,LB:Lower bound, UB:Upper bound (Upper or lower bounds ie. critical zones)
#
# Requsts for values between two timestamps are therefore
# T:,T:,N:,N,N,...
#
# The answer to the request will be
# N:,T:,V:,T:,V:...(LB:,UB:)
# Depending on how many values there are (Bounds can be omitted)


def handle_request(msg):
    offset = 0
    # this method generates a list with the data format [T,T] + [N,N...]
    tagList = []
    timestampList = []

    # Find the two timestamps
    for x in range(2):
        foundToken, timestamp, offset = disect_string(msg, 'T:', offset)
        if (not foundToken):
            timestamp = str(datetime.datetime.now())
        timestampList.append(timestamp)

    # Loop through the string and pick the tagnumbers and timestamps
    while offset < len(msg):
        # Find tag number
        foundToken, tagNr, offset = disect_string(msg, 'N:', offset)
        if (not foundToken):
            break

        tagList.append(tagNr)
    
    response = generate_response(timestampList, tagList)
    return response


def disect_string(msg, token, offset):
    oldOffset = offset
    offset = msg.find(token, offset)
    # If we find no value then we have reached the end of the message
    if offset == -1:
        return False, "", oldOffset

    # Offset the pointer to not include N:
    offset += 2
    # Get the offset to the next comma
    nextComma = msg.find(',', offset)
    # Get the value between the comma and the pointer
    disectedString = msg[offset:nextComma]
    offset = nextComma
    return True, disectedString, offset


def generate_response(timestamps, tagnumbers):

    response = ''

    startTime = datetime.datetime.strptime(timestamps[0], DATETIMEFORMAT)
    endTime = datetime.datetime.strptime(timestamps[1], DATETIMEFORMAT)
    print("tagnumbers length:", len(tagnumbers))
    for element in tagnumbers:
        response += 'N:' + element + ','
        response += 'T:' + timestamps[0] + ','
        response += 'V:' + generate_value(element) + ','
        i = 15
        for x in range(i):
            date_time = (startTime + ((x + 1) / (i + 2)) *
                         (endTime - startTime)).replace(microsecond=0)

            # Limit the data points to be per 10 seconds.
            # This has no effect on the outcome of the data
            # It is just while we are using random numbers
            # If this is not here there will be double data points on the graph when reloading
            # Since we are removing duplicates timestamps
            date_time = date_time.replace(
                second=(floor(date_time.second / 10) * 10))

            response += 'T:' + date_time.strftime(DATETIMEFORMAT) + ','
            response += 'V:' + generate_value(element) + ','
        response += 'T:' + timestamps[1] + ','
        response += 'V:' + generate_value(element) + ','

        response += generate_boundaries(element)

    print(response)
    return response


def generate_value(element):
    if (element == '820_STDEV_WIC_130'):
        return (str(random.uniform(0, 4.2)))
    elif (element == '820_HIC_175'):
        return (str(random.uniform(0.0, 90.0)))
    elif (element == '820_TT_313A'):
        return (str(random.uniform(0.0, 415.8)))
    elif (element == '820_HIC_176'):
        return (str(random.uniform(0.0, 80.0)))
    elif (element == '820_TT_175'):
        return (str(random.uniform(0.0, 66.2)))
    elif (element == '820_STDEV_WIC_120'):
        return (str(random.uniform(0, 15.8)))
    elif (element == '820_TT_312A'):
        return (str(random.uniform(0.0, 365.8)))
    elif (element == '820_WQT_110'):
        return (str(random.uniform(0.0, 7.0)))
    elif (element == '820_FT_171'):
        return (str(random.uniform(0.0, 15.0)))
    elif (element == '820_WQT_160'):
        return (str(random.uniform(0.0, 20.0)))
    elif (element == '820_WQT_100'):
        return (str(random.uniform(0.0, 20.0)))
    elif (element == '820_TT_314B'):
        return (str(random.uniform(0.0, 435.3)))
    elif (element == '820_TT_314A'):
        return (str(random.uniform(0.0, 43.5)))
    elif (element == 'HTZ-1 porevolume'):
        return (str(random.uniform(LOWER_REJ_HTZ_1 - 2, UPPER_REJ_HTZ_1 + 2)))
    elif (element == 'HTZ-3 porevolume'):
        return (str(random.uniform(LOWER_REJ_HTZ_3 - 2, UPPER_REJ_HTZ_3 + 2)))
    elif (element == 'HTZ-31 porevolume'):
        return (str(random.uniform(LOWER_REJ_HTZ_31 - 2, UPPER_REJ_HTZ_31 + 2)))
    elif (element == 'HTZ-5 porevolume'):
        return (str(random.uniform(LOWER_REJ_HTZ_5 - 2, UPPER_REJ_HTZ_5 + 2)))
    elif (element == 'HTZ-51 porevolume'):
        return (str(random.uniform(LOWER_REJ_HTZ_51 - 2, UPPER_REJ_HTZ_51 + 2)))
    else:
        return (str(random.uniform(100.0, 200.0)))


def generate_boundaries(element):
    if (element == 'HTZ-1 porevolume'):
        return ('B:' + str(LOWER_REJ_HTZ_1) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(UPPER_REJ_HTZ_1) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(LOWER_TOL_HTZ_1) + ',' + 'C:' + ORANGE_BOUND_COL + ',' +
                'B:' + str(UPPER_TOL_HTZ_1) + ',' + 'C:' + ORANGE_BOUND_COL + ',')
    elif (element == 'HTZ-3 porevolume'):
        return ('B:' + str(LOWER_REJ_HTZ_3) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(UPPER_REJ_HTZ_3) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(LOWER_TOL_HTZ_3) + ',' + 'C:' + ORANGE_BOUND_COL + ',' +
                'B:' + str(UPPER_TOL_HTZ_3) + ',' + 'C:' + ORANGE_BOUND_COL + ',')
    elif (element == 'HTZ-31 porevolume'):
        return ('B:' + str(LOWER_REJ_HTZ_31) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(UPPER_REJ_HTZ_31) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(LOWER_TOL_HTZ_31) + ',' + 'C:' + ORANGE_BOUND_COL + ',' +
                'B:' + str(UPPER_TOL_HTZ_31) + ',' + 'C:' + ORANGE_BOUND_COL + ',')
    elif (element == 'HTZ-5 porevolume'):
        return ('B:' + str(LOWER_REJ_HTZ_5) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(UPPER_REJ_HTZ_5) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(LOWER_TOL_HTZ_5) + ',' + 'C:' + ORANGE_BOUND_COL + ',' +
                'B:' + str(UPPER_TOL_HTZ_5) + ',' + 'C:' + ORANGE_BOUND_COL + ',')
    elif (element == 'HTZ-51 porevolume'):
        return ('B:' + str(LOWER_REJ_HTZ_51) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(UPPER_REJ_HTZ_51) + ',' + 'C:' + RED_BOUND_COL + ',' +
                'B:' + str(LOWER_TOL_HTZ_51) + ',' + 'C:' + ORANGE_BOUND_COL + ',' +
                'B:' + str(UPPER_TOL_HTZ_51) + ',' + 'C:' + ORANGE_BOUND_COL + ',')
    else:
        return ""

#def data_processing():
    

"""
# Generate random data to send to client
def data_generation():
    TIMESTAMP = str(datetime.datetime.now())
    VALUE = str(random.uniform(100, 200))
    data = '{' + TAGNRS[0] + ': [' + TIMESTAMP + ', ' + VALUE + '], ' + TAGNRS[1] + ': [' + \
        TIMESTAMP + ', ' + VALUE + '], ' + \
        TAGNRS[2] + ': [' + TIMESTAMP + ', ' + VALUE + ']}'
    return data
"""


# Start function to initialize server and open threads
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()

        # Initialize thread to handle client connections
        connection_manager_thread = threading.Thread(
            target=handle_client, args=(conn, addr))
        connection_manager_thread.start()

        #data_processing_thread = threading.Thread(
        #    target=data_processing, args=())
        #data_processsing_thread.start()

        # Initialize other threads: collect data, train ML models, run simulations, etc.
        #data_generation_thread = threading.Thread(target=data_generation)
        # data_generation_thread.start()

        # Check how many active client connections are currently active
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    # Main function
if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start()
