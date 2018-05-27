from redis import StrictRedis
from redlock_dist import RedLock

if __name__ == '__main__':
    rds = StrictRedis(host='localhost', port=6379, db=0)
    with RedLock(rds, 'key-name') as red_lock:
        if red_lock:
            print('get lock')
        else:
            print('do not get lock')
