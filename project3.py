import package.read_edit_file as edit_file
from multiprocessing import Pool

import time
def main():
    total_run = 1
    file_name = "test4.txt"
    time_seq = 0
    process = 8 # number of process of MAPR
    word = edit_file.split_file(file_name)
    # Sequencial
    for i in range (total_run):
        t1 = time.time()
        word_tracking_seq = edit_file.read_count_seq(word)
        time_seq += time.time() - t1
    time_seq = time_seq / total_run
    print("Total words: %d" %len(word))
    print ( "Time sequencial: %4.4f \n" % time_seq )
    # MapR
    for p in range(2, process+1):
        time_mapr = 0
        pool = Pool ( p )
        input ( "Press enter to continue" )
        for i in range (total_run):
            t2 = time.time()
            word_tracking_mapr = edit_file.read_count_MapR(pool, p, word)
            time_mapr += time.time() - t2
        pool.close()
        pool.join()
        time_mapr = time_mapr / total_run
        print("Time MapR: %4.4f with %d processes\n" % (time_mapr, p))

if __name__ == "__main__":
    main()
