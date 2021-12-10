import os


class CommunicationViaTxt:
    __m_file = ""   # Path or, if file is in same directory, Filename

    def connect(self, file):
        self.__m_file = file
        if os.path.isfile("open_" + self.__m_file):
            return 1
        try:
            f = open(self.__m_file, "x")
            f.close()
            self.write_once('')
            return 0
        except:
            return 1

    def write_once(self, data):
        try:
            os.rename(self.__m_file, "open_" + self.__m_file)

            f = open("open_" + self.__m_file, 'w')
            f.write(data)
            f.close()

            os.rename("open_" + self.__m_file, self.__m_file)
            return(0)
        except:
            return(1)

    def append_once(self, data):
        try:
            os.rename(self.__m_file, "open_" + self.__m_file)

            f = open("open_" + self.__m_file, 'a')
            f.write(data)
            f.close()

            os.rename("open_" + self.__m_file, self.__m_file)
            return(0)
        except:
            return(1)

    def write_keep_trying(self, data, retakes, delayseconds):
        for i in range(retakes-1):
            try:
                os.rename(self.__m_file, "open_" + self.__m_file)

                f = open("open_" + self.__m_file, 'w')
                f.write(data)
                f.close()

                print(i)

                os.rename("open_" + self.__m_file, self.__m_file)
                return [0, i+1]
            except:
                pass
            time.sleep(delayseconds)
        return 1

    def append_keep_trying(self, data, retakes, delayseconds):
        for i in range(retakes):
            try:
                os.rename(self.__m_file, "open_" + self.__m_file)

                f = open("open_" + self.__m_file, 'a')
                f.write(data)
                f.close()

                os.rename("open_" + self.__m_file, self.__m_file)
                return [0, i]
            except:
                pass
            time.sleep(delayseconds)
        return 1

    def read_once(self):
        try:
            os.rename(self.__m_file, "open_" + self.__m_file)

            f = open("open_" + self.__m_file, 'r')
            data = f.read()
            f.close()
            open("open_" + self.__m_file, 'w').close()

            os.rename("open_" + self.__m_file, self.__m_file)
            return data
        except:
            return "offen"
