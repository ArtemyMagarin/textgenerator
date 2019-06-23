# Yet another Markov Chain based text generator

## How to use it
```bash
python3 -m textgenerator <input_file> <window_size> <sentences_count>
```

Where:
- __input_file__ - text file for build a model
- __window_size__ - number 
- __sentences_count__ - number of sentences you want to generate

You can create your own assets to teach a model or use included assets,
for example:

```bash
python3 -m textgenerator assets/pikabu.txt 2 10
```

creates 10 sentences length dummy pikabu post.



## License

__MIT__