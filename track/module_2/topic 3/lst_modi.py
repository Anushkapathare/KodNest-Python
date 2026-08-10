original_scores = []
for i in range(3):
 original_scores.append(int(input()))

alias_scores = original_scores

replacement_score = int(input())
additional_score = int(input())

alias_scores[0] = replacement_score
alias_scores.append(additional_score)

print(original_scores)
print(alias_scores)
print(original_scores == alias_scores)
