def truncate_sentence(s,k):
    words= s.split()
    truncate_words=words[:k]
    truncated_sentence=''(truncated_words)
    return truncated_sentence
sentence = "hello how are you"
k=3
truncated = truncate_sentence(sentence,k)
print(truncated)