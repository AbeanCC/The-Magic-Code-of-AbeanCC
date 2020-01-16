import hashlib

'''
每个区块链都有三个部分组成
    数据
    自己的hash (hash = H(data + Previous hash))
    前一个节点的hash(Previous hash)
'''

'''Block'''

class Block:
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.ownhash = self.ComputeHash()

    def ComputeHash(self):
        '''计算Hash值'''
        sha256 = hashlib.sha256()
        sha256.update((str(self.data) + self.previousHash).encode("utf-8"))
        return sha256.hexdigest()

    def StandardOutput(self):
        '''标准化输出'''
        print("Block:\n\t\tData: {}\n\t\tOwnHash: {}\n\t\tPreviousHash: {}".format(self.data, self.ownhash, self.previousHash), end="\n")

'''Chain'''

class Chain:
    def __init__(self):
        self.chainlist = [self.GenesisBlock()]

    def GenesisBlock(self):
        '''创建祖先区块'''
        return Block("Genesis", "")

    def InsertNewBlock(self, data):
        '''插入新的区块'''
        newblock = Block(data, self.chainlist[-1].ownhash)
        self.chainlist.append(newblock)

    def StandardOutput(self):
        '''标准化输出'''
        print("Chain:\n", end="")
        for i in range(0, len(self.chainlist)):
            print("",end="\t")
            self.chainlist[i].StandardOutput()

    def ValidateChain(self):
        '''验证区块链是否合法'''
        for i in range(1, len(self.chainlist)):
            if self.chainlist[i].ownhash == self.chainlist[i].ComputeHash():
                if self.chainlist[i].previousHash != self.chainlist[i-1].ownhash:
                    print("前后区块链断裂")
                    return False
                else:
                    continue
            else:
                print("数据被篡改")
                return False
        return True

'''然后你就可以尝试增加区块'''

if __name__ == "__main__":
    chain = Chain()
    chain.InsertNewBlock("我有十块钱")
    chain.InsertNewBlock("我有二十块钱")
    chain.InsertNewBlock("我有三十块钱")
    chain.InsertNewBlock("我有四十块钱")
    chain.InsertNewBlock("我有五十块钱")
    chain.StandardOutput()
    print(chain.ValidateChain())


