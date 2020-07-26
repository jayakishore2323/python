s='azzbcdabbcdabbccccddeeef'
output=""

for i in s:
    if i not in output:
        output+=i
print(output)