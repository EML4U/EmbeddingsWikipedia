import numpy

class DataAccess:
    
    # Data:
    # https://hobbitdata.informatik.uni-leipzig.de/EML4U/2021-02-10-Wikipedia-Texts/
    # https://hobbitdata.informatik.uni-leipzig.de/EML4U/2021-04-07-Wikipedia-Embeddings/
    
    # Directories in source_texts_directory
    # 20100408-american-films
    # 20100408-british-films
    # 20100408-Indexes
    # 20100408-indian-films
    # 20100408-living-people
    # 20201101-american-films
    # 20201101-british-films
    # 20201101-Indexes
    # 20201101-indian-films
    # 20201101-living-people

    # Files in embeddings_directory
    # 20100408-american-films.txt
    # 20100408-british-films.txt
    # 20100408-indian-films.txt
    # 20201101-american-films.txt
    # 20201101-british-films.txt
    # 20201101-indian-films.txt
    # american-films.txt
    # british-films.txt
    # indian-films.txt
    
    # e.g. "/home/eml4u/EML4U/data/corpus/2021-02-10-wikipedia-texts/","/home/eml4u/EML4U/data/wikipedia-embeddings/"
    def __init__(self, source_texts_directory, embeddings_directory):
        self.source_texts_directory = source_texts_directory
        self.embeddings_directory = embeddings_directory
        self.wikipedia_dict = {}
        self.embeddings_dict = {}

    # Source texts from Wikipedia

    # e.g. "20100408-british-films", "Monty_Python_s_The_Meaning_of_Life.txt"
    def read_source_text(self, directory, filename, print_filepath = True):
        filepath = self.source_texts_directory + directory + "/" + filename
        if print_filepath:
            print(filepath)
        file = open(filepath, "r") 
        text = file.read() 
        file.close()
        return text
    
    # Index filenames <-> Wikipedia titles

    # e.g. "20100408", "british-films"
    def get_wikipedia_dict(self, time_id, category_id):
        filepath = self.source_texts_directory + time_id + "-Indexes/Index_Category_" + category_id.capitalize().replace('-', '_') + ".txt"
        count = 0
        dictionary = {}
        id = ""
        with open(filepath) as fileobject:
            for line in fileobject:
                line = line[:-1]
                if count % 2 == 0:
                    id = line
                else:
                    if not line:
                        break
                    else:
                        dictionary[id] = line
                count += 1
        return dictionary
    
    # e.g. "20100408", "british-films", "Monty_Python_s_The_Meaning_of_Life.txt"
    def get_wikipedia_dict_title(self, time_id, category_id, filename):
        id = time_id + "-" + category_id
        if(id not in self.wikipedia_dict):
            self.wikipedia_dict[id] = self.get_wikipedia_dict(time_id, category_id)
        return self.wikipedia_dict[id][filename];
    
    # e.g. "20100408", "british-films", "Monty Python's The Meaning of Life"
    def get_wikipedia_dict_filename(self, time_id, category_id, title):
        id = time_id + "-" + category_id
        if(id not in self.wikipedia_dict):
            self.wikipedia_dict[id] = self.get_wikipedia_dict(time_id, category_id)
        return list(self.wikipedia_dict[id].keys())[list(self.wikipedia_dict[id].values()).index(title)]

    # Embeddings
    
    # e.g. "20100408-british-films"
    def load_embeddings(self, file_id, print_filename = True, print_info = True):
        filename = self.embeddings_directory + file_id + ".txt"
        if print_filename:
            print(filename)
        embeddings = numpy.loadtxt(self.embeddings_directory + file_id + ".txt")
        if print_info:
            print(embeddings.shape, type(embeddings))
        return embeddings
    
    # Index embeddings filenames
    
    # e.g. "british-films", 189
    def get_embeddings_dict_filename(self, category_id, index):
        indexFilename = category_id + ".txt"
        if(category_id not in self.embeddings_dict):
            with open(self.embeddings_directory + indexFilename) as f:
                self.embeddings_dict[category_id] = f.read().splitlines()
        return self.embeddings_dict[category_id][index];

    # e.g. "british-films", "Monty_Python_s_The_Meaning_of_Life.txt"
    def get_embeddings_dict_index(self, category_id, filename):
        indexFilename = category_id + ".txt"
        if(category_id not in self.embeddings_dict):
            with open(self.embeddings_directory + indexFilename) as f:
                self.embeddings_dict[category_id] = f.read().splitlines()
        return self.embeddings_dict[category_id].index(filename)


# Examples

# Example: Imports and definitions
if False:
    import data_access
    source_texts_directory = "/home/eml4u/EML4U/data/corpus/2021-02-10-wikipedia-texts/"
    embeddings_directory  = "/home/eml4u/EML4U/data/wikipedia-embeddings/"
    data_accessor = data_access.DataAccess(source_texts_directory, embeddings_directory)
    
    id_a = "20100408"
    id_british  = "british-films"
    id_british_a  = id_a + "-" + id_british
    filename = "Monty_Python_s_The_Meaning_of_Life.txt"
    title = "Monty Python's The Meaning of Life"

# Source texts from Wikipedia
    
# Example: Read source text
if False:
    print(len(data_accessor.read_source_text(id_british_a, filename)))
    print()

# Index filenames <-> Wikipedia titles

# Example: 
if False:
    print(len(data_accessor.get_wikipedia_dict(id_a, id_british)))
    print()

# Example: 
if False:
    print(data_accessor.get_wikipedia_dict_title(id_a, id_british, filename))
    print()

# Example: 
if False:
    print(data_accessor.get_wikipedia_dict_filename(id_a, id_british, title))
    print()
    
# Embeddings
    
# Example: Load embeddings
if False:
    print(data_accessor.load_embeddings(id_british_a).shape);
    print()

# Index embeddings filenames

# Example: Look up index
if False:
    print(data_accessor.get_embeddings_dict_filename(id_british, 189))
    print()
    
# Example: Look up filename
if False:
    print(data_accessor.get_embeddings_dict_index(id_british, filename))
    print()
