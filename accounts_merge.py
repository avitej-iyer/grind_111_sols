class UnionFind:
    def __init__(self, num):
        self.parent = list(range(num))

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]    

    def union(self, child, parent):
        self.parent[(self.find(child))] = self.find(parent)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        ownership = {}
        for i, (_,*emails) in enumerate(accounts):
            for mail in emails:
                if mail in ownership:
                    uf.union(i, ownership[mail])
                ownership[mail] = i    

        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]]+ sorted(emails) for i, emails in ans.items()]            