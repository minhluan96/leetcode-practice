import queue

class Solution:
    def thatIsYourQueue(self, P, C, commands):
        hospitalQueue = queue.Queue()
        for i in range(1, min(P, C) + 1):
            hospitalQueue.put(i)

        for k in range(C):
            cmd = commands[k]
            if cmd[0] == 'N':
                value = hospitalQueue.get()
                print(value)
                hospitalQueue.put(value)
            else:
                x = cmd[1]
                n = hospitalQueue.qsize()
                hospitalQueue.put(x)
                for j in range(n):
                    temp = hospitalQueue.get()
                    if temp != x:
                        hospitalQueue.put(temp)


    def answer(self, P, C, commands):
        '''
        De thêm hoặc bốc x ra thì có thể sử dụng xoay vòng x
        b1: Thêm x vào cuối hàng
        b2: lần lượt chuyểnn 1 2 3 ... N về cuối hàng TRỪ x
        NOTE: chỉ xử lý C thao tác
        Nếu x nằm ở khoảng > C thì ta có thể bỏ x thẳng vào đầu hàng vd: x 1 2 (với C = 2)
        Độ phức tạp O(min(P, C)^2)

        Mã giả
        while(true):
            nhaajp P, C
            nếu P == 0 và C == 0
                exit

            queue
            for i: 1 -> min(P, C):
                queue.add(i)

            Nhap thao tac chr
            Neu chr == N:
                in queue.top()
                queue.add(queue.top())
                queue.remove()


        '''
        hospitalQueue = queue.Queue()
        for i in range(min(P, C)):
            hospitalQueue.put(i + 1)


        for i in range(min(P, C)):
            if  i == 'N':
            value = hospitalQueue.get()
            print(value)
            else:
                hospitalQueue.put(commands[i])
                for i in range(hospitalQueue.qsize()):
                    value = hospitalQueue.get()
                    if value != commands[i]:
                        hospitalQueue.put(value)

                    

if __name__ == '__main__':
    counter = 1

    while True:
        firstLine = list(map(int, input().split()))
        if firstLine[0] == 0 and firstLine[1] == 0:
            break

        P = firstLine[0]
        C = firstLine[1]

        print('Case {}:'.format(counter))
        counter += 1

        commands = []

        for i in range(C):
            command = input().split()
            if len(command) > 1:
                commands.append((command[0], int(command[1])))
            else:
                commands.append((command[0], ))

        solution = Solution()
        solution.thatIsYourQueue(P, C, commands)

