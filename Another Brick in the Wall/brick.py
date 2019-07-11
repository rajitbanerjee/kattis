"""https://open.kattis.com/problems/anotherbrick"""

h, w, _ = map(int, input().split())
bricks = list(map(int, input().split()))

width, complete = w, False
for b in bricks:
    if not complete:
        if b > w:
            # failed, if length of brick is more than wall width
            complete = -1
        else:
            # add next brick to the wall
            w -= b
            if w == 0:
                # current layer is complete
                w = width
                # move to next layer
                h -= 1
            # update completion status
            complete = (h == 0)

print("NO") if complete == -1 else print("YES")
