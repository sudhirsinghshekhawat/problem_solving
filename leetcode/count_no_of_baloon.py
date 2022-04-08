balloon_dict = {i: 0 for i in set("balloon")}
string = "nlaebolko"
for ch in string:
    if ch in balloon_dict:
        balloon_dict[ch] = balloon_dict.get(ch, 0) + 1
balloon_dict['l'] = balloon_dict['l'] // 2
balloon_dict['o'] = balloon_dict['o'] // 2

print(min(balloon_dict.values()))

