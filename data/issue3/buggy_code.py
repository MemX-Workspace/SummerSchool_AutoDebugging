class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        self.r = len(pizza)
        self.c = len(pizza[0])

        # Step 1, pre-process the apple array and get the prefix sum
        tot_apples = 0
        self.pfsum_row = []
        self.pfsum_col = []

        for i in range(self.r):
            pfr = 0
            pfs_r = [0] * self.c
            pfs_c = [0] * self.c
            for j in range(self.c):
                if i > 0:
                    pfs_c[j] += self.pfsum_col[i - 1][j]
                if pizza[i][j] == 'A':
                    pfr += 1
                    pfs_c[j] += 1
                    tot_apples += 1
                pfs_r[j] = pfr
            self.pfsum_row.append(pfs_r)
            self.pfsum_col.append(pfs_c)

        if tot_apples < k:
            return 0

        if k == 1:
            return 1

        return self.getWays(0, 0, k - 2) % (1000000007)

    @cache
    def getWays(self, i, j, k):
        if k == 1:
            # if only left one piece for cutting, we just need to check if there is any apple in the region
            found = False
            for c in range(j, self.c):
                apple_in_region = self.pfsum_col[self.r - 1][c]
                if i > 0:
                    apple_in_region -= self.pfsum_col[i - 1][c]
                if apple_in_region:
                    found = True
                    break
            if found:
                return 1
            return 0
        else:
            # horizontally cut
            cannot_cut = True
            nr = i
            t_cnt = 0
            while nr < self.r - 1:
                # find the first row that we can start cutting
                while nr < self.r - 1 and cannot_cut:
                    apple_in_region = self.pfsum_row[nr][self.c - 1]
                    if j > 0:
                        apple_in_region -= self.pfsum_row[nr][j - 1]
                    if apple_in_region:
                        cannot_cut = False
                    else:
                        nr += 1

                if nr < self.r - 1:
                    t_cnt += self.getWays(nr + 1, j, k - 1)
                nr += 1

            # vertically cut
            cannot_cut = True
            nc = j
            while nc < self.c - 1:
                # find the first col that we can start cutting
                while nc < self.c - 1 and cannot_cut:
                    apple_in_region = self.pfsum_col[self.r - 1][nc]
                    if i > 0:
                        apple_in_region -= self.pfsum_col[i - 1][nc]
                    if apple_in_region:
                        cannot_cut = False
                    else:
                        nc += 1

                if nc < self.c - 1:
                    t_cnt += self.getWays(i, nc + 1, k - 1)
                nc += 1

            return t_cnt