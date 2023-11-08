# write a program to genrate mutlipication table from 2 to 20 and
# write it to the different files.place these files in a folder for a
# 13-year old guy.

for i in range(2, 21):
    with open(f"tables/mutlipication_table_of_{i}.txt", 'w')as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}\n")