# CLIP FILTER
#copy the whole discord channel and paste it in rawchannel.txt in the same folder that find link.py is in
#the script will make a file called links.txt with all unique link from the discord channel



arr = []
alreadylinked=False
with open("rawchannel.txt", 'r+') as f:
	for line in f:
		alreadylinked=False
		if(line[0:32]=="https://www.twitch.tv/m0xyy/clip"):
			for i in range(len(line)):
				if (line[i]=="?"):
					line = line[0:i]+"\n"
					break
			for link in arr:
				if line == link:
					alreadylinked=True
			if (not alreadylinked):
				arr.append(line)
print(arr)
with open("links.txt", 'w') as f:
	for i in arr:
		f.write(i)

