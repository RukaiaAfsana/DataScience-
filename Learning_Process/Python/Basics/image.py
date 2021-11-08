with open('2D9A2273.CR2','rb') as rp:
    with open('new_2D9A2273.CR2' , 'wb') as wp:
        rp_contents = rp.read()
        wp.write(rp_contents)

with open('2D9A2273.CR2','rb') as rp:
    with open('newEdited_2D9A2273.CR2' , 'wb') as wp:
        chunk_size = 1080
        rp_contents = rp.read(chunk_size)
        while len(rp_contents) > 0 :
            wp.write(rp_contents)
            rp_contents = rp.read(chunk_size)