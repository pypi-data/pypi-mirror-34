# pypexels\_l5

An open source Python wrapper for the [Pexels REST
API](https://www.pexels.com/api/), supporting Python 2.7 and 3.6+. This is
[Lumen5's](https://lumen5.com) fork of [salvoventura's
work](https://github.com/salvoventura/pypexels).

## Note

When using this library you still need to abide by Pexels guidelines,
which are explained on [Pexels' API page](https://www.pexels.com/api/)

# Examples

This example shows how the interaction with the paging functionality of
the Pexels API is greatly abstracted and simplified. The code below will
iterate through all popular images, and print attributes for each photo
in there.

```python
from pypexels import PyPexels
api_key = 'YOUR_API_KEY'

# instantiate PyPexels object
py_pexels = PyPexels(api_key=api_key)

popular_photos = py_pexels.popular(per_page=30)
while popular_photos.has_next:
    for photo in popular_photos.entries:
        print(photo.id, photo.photographer, photo.url)
    # no need to specify per_page: will take from original object
    popular_photos = popular_photos.get_next_page()
```

`pypexels_l5` is released under the [MIT
License](http://www.opensource.org/licenses/MIT).
