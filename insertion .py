#kochi metro card users fequent tranvelers list
travel_count=[['aluva', 20], ['Pulinchodu', 40], ['Companypadi', 40], ['Ambattukavu', 50], ['Muttom', 60], ['Kalamassery', 70], ['Pathadipalam', 80], ['Edapally', 90], ['Changampuzha Park', 60], ['Palarivattom', 80], ['JLN Stadium', 40], ['Kaloor', 30], ['Town Hall', 20], ['MG Road', 90], ['Maharajas College', 10], ['Ernakulam South', 50], ['Kadavanthara', 90], ['Elamkulam', 20], ['Vyttila', 20], ['Thykoodam', 90], ['Petta', 60]]
def insertion_sort(travel_count):
    for j in range(1,len(travel_count)):
        key=travel_count[j][1]
        keyv=travel_count[j]
        i=j-1
        while i>=0 and travel_count[i][1]>key:
            travel_count[i+1]=travel_count[i]
            i-=1
        travel_count[i+1]=keyv
    return travel_count

print(insertion_sort(travel_count))
    