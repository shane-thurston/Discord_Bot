#underneath the new Discord instance
sad_words = [
  "sad", 
  "depressed", 
  "unhappy", 
  "angry", 
  "miserable", 
  "depressing"
]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

#inside main msg loop
if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
    
if msg.startswith('$hello'):
    await message.channel.send('Hello')
    emoji = '\N{THUMBS UP SIGN}'
    await message.add_reaction(emoji)
    
if any(word in msg for word in harm_words):
    await message.author.send("Suicide website link")
    
if msg in bullying:
    await message.delete()
