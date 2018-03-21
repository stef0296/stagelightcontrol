import eyeD3
tag = eyeD3.Tag()
tag.link("/some/file.mp3")
print(tag.getArtist())
print(tag.getAlbum())
print(tag.getTitle())
