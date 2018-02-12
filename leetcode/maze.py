class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        n_row = len(maze)
        n_col = len(maze[0])
        
        ball = tuple(ball)
        hole = tuple(hole)
        # determine the neighbors (can use closures)
        def neighbors(r, c):
            # for directions
            
            for dr, dc, di in [(0, 1, 'r'), (0, -1, 'l'), (-1, 0, 'u'), (1, 0, 'd')]:
                # dr is the distance for rows
                # dc is the distance for columns
                cur_r = r
                cur_c = c
                dist = 0
                while (0 <=  cur_r+dr < n_row and
                       0 <= cur_c+dc < n_col and
                       maze[cur_r+dr][cur_c+dc]==0):
                    cur_r += dr
                    cur_c += dc
                    dist += 1
                    if (cur_r, cur_c) == hole:
                        break
                yield ((cur_r, cur_c), di, dist)
        
        ### main : using dijkstra's algorithms
        # initialize
        pq = [(0, '', ball)]
        seen = set()
        while pq:
            dist, path, node = heapq.heappop(pq)
            
            if node in seen: 
                continue
            if node == hole:
                return path
            
            seen.add(node)
            print node
            print "neighbors: "
            for n_node, n_di, n_dist in neighbors(*node):
                print n_node
                heapq.heappush(pq, (n_dist+dist, path+n_di , n_node))
        
        return "impossible" 