import csv

def main(start,end):
    # อ่านแผนที่จากไฟล์ csv 
    with open(filename,encoding="utf-8", newline='') as csvfile:
        reader = csv.reader(csvfile)
        roads = []
        for row in reader:
            roads.append(row) 
    
    # สร้าง dict เก็บชื่อเมืองและระยะทาง
    dict_csv = {}
    for row in roads:
        node1 = row[0]
        node2 = row[1]
        if node1 not in dict_csv:
            dict_csv[node1] = []
        if node2 not in dict_csv:
            dict_csv[node2] = []
        if row == roads[0] :
            dict_csv[node1].append(node2)
            dict_csv[node2].append(node1)
        else :
            dict_csv[node1].append(node2)
    
    # หาเส้นทางที่เป็นไปได้ทั้งหมดของเมืองเริ่มต้นจนถึงเมืองสุดท้าย
    paths = find_all_paths(dict_csv, start, end)
    # คำนวณระยะทางของแต่ละเส้นทางที่เป็นไปได้
    all_sum_distance = sum_distance (paths,roads)         
    
# function หาเส้นทางที่เป็นไปได้ทั้งหมดของเมืองเริ่มต้นจนถึงเมืองสุดท้าย
def find_all_paths(dict_csv, start, end):
    # สร้าง list เก็บเส้นทางที่เป็นไปได้ทั้งหมด
    paths = []
    stack = [(start, [start])]

    while stack :
        node, path = stack.pop()
        if node == end:
            paths.append(path)
        for p in dict_csv[node]:
            if p not in path:
                stack.append((p, path + [p]))
    return paths

# สร้างฟังก์ชันไว้หาผลรวมระยะทาง
def sum_distance (paths,roads) :
    answer = []
    data = []
    data1 = []
    long = []
    sum_dist = []
    min_dist = []

    #เอาระยะทางทั้งหมดที่อยู่ใน path นั้น ใส่ไว้ใน list (sum_dist)
    
    for path in paths :
        for i in roads :
            for y in range (0 , len(path)) :
                if (i[0] in (path[y-2])) and (i[1] in path[y-1] ):
                    long.append(int(i[2]))
            sum_dist.append(long)
            long = []

        # append path และระยะทางรวมลงไปใน list data แล้วนำค่าจาก list data ไปใส่ไว้ใน list data1 อีกที
        data.append(path)
        data.append(sum_sublists(sum_dist))
        data1.append(data)
        data = []

        # แปลง data1 จาก list เป็น dictionary โดยมีค่า key เป็น path และ distance
        for i in range (0,len(data1)) :
            answer1 = {'path': data1[i][0], 'Distance': data1[i][1]}
            answer.append(answer1)
        min_dist.append(sum_sublists(sum_dist))
        sum_dist = []

    # เทียบค่า distance เพื่อหา path ที่มีระยะทางรวมสั้นที่สุด
    x = 0
    while True : 
        if answer[x]['Distance'] == min(min_dist) :
            print('-'*50)
            print('Shortest Path = {} Distance = {}'.format((answer[x]['path']),(answer[x]['Distance'])))
            print('-'*50)
            break
        x += 1

# นำค่าจาก sum_dist มารวมกันเป็นระยะทางรวม
def sum_sublists(value):
    total_sum = 0
    for sublist in value:
        if sublist:
            total_sum += sum(sublist)
    return total_sum

if __name__ == '__main__':
    print('-'*50)
    filename = input('Enter file name : ')
    main(input('Enter first city : '),input('Enter last city : '))