"""https://open.kattis.com/problems/musicalscales"""

def main():
    num = int(input())
    notes_played = input().split()
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    scales = {}
    for each in notes:
        scales[each] = findScale(each, notes)
    
    ans = ""
    for note, scale in scales.items():
        count = 0
        for n in notes_played:
            if n in scale:
                count += 1
        if count == num:
            ans += note + " "

    if len(ans) == 0:
        print("none")
    else:
        print(ans)
                

def findScale(note, notes):
    i, scale = notes.index(note), []
    while len(scale) != 8:
        scale.append(notes[i])
        jump = 1 if (len(scale) in [3, 7]) else 2
        i = (i + jump) % 12
    return scale

if __name__ == '__main__':
    main()
