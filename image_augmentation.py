import matplotlib.pyplot
%matplotlib inline

# Flipping images with Numpy
flipped_img = np.fliplr(img)
plt.imshow(flipped_img)
plt.show()

#______Translations_____
# Shifting Left
for i in range(HEIGHT, 1, -1):
  for j in range(WIDTH):
     if (i < HEIGHT-20):
       img[j][i] = img[j][i-20]
     elif (i < HEIGHT-1):
       img[j][i] = 0

plt.imshow(img)
plt.show()

# Shifting Right
for j in range(WIDTH):
  for i in range(HEIGHT):
    if (i < HEIGHT-20):
      img[j][i] = img[j][i+20]

plt.imshow(img)
plt.show()


# Shifting Up
for j in range(WIDTH):
  for i in range(HEIGHT):
    if (j < WIDTH - 20 and j > 20):
      img[j][i] = img[j+20][i]
    else:
      img[j][i] = 0

plt.imshow(img)
plt.show()

#Shifting Down
for j in range(WIDTH, 1, -1):
  for i in range(278):
    if (j < 144 and j > 20):
      img[j][i] = img[j-20][i]

plt.imshow(img)
plt.show()

# ADDING NOISE
noise = np.random.randint(5, size = (164, 278, 4), dtype = 'uint8')

for i in range(WIDTH):
    for j in range(HEIGHT):
        for k in range(DEPTH):
            if (img[i][j][k] != 255):
                img[i][j][k] += noise[i][j][k]
plt.imshow(img)
plt.show()
