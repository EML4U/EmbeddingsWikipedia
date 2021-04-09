import numpy

class DataAccess:
    
    # Data:
    # https://hobbitdata.informatik.uni-leipzig.de/EML4U/2021-02-10-Wikipedia-Texts/
    # https://hobbitdata.informatik.uni-leipzig.de/EML4U/2021-04-07-Wikipedia-Embeddings/
    
    # e.g. "/home/eml4u/EML4U/data/corpus/2021-02-10-wikipedia-texts/","/home/eml4u/EML4U/data/wikipedia-embeddings/"
    def __init__(self, source_texts_directory, embeddings_directory):
        self.source_texts_directory = source_texts_directory
        self.embeddings_directory = embeddings_directory
        self.embeddings_dict = {}
                
    # e.g. "20201101-american-films", "Pirates_of_Tortuga.txt"
    def read_source_text(self, directory, filename, print_filepath = True):
        filepath = self.source_texts_directory + directory + "/" + filename
        if print_filepath:
            print(filepath)
        file = open(filepath, "r") 
        text = file.read() 
        file.close()
        return text

    # e.g. "american-films", 0
    def get_source_text_filename(self, category_id, index):
        indexFilename = category_id + ".txt"
        if(category_id not in self.embeddings_dict):
            with open(self.embeddings_directory + indexFilename) as f:
                self.embeddings_dict[category_id] = f.read().splitlines()
        return self.embeddings_dict[category_id][index];

    # e.g. "american-films", "Pirates_of_Tortuga.txt"
    def get_source_text_index(self, category_id, filename):
        indexFilename = category_id + ".txt"
        if(category_id not in self.embeddings_dict):
            with open(self.embeddings_directory + indexFilename) as f:
                self.embeddings_dict[category_id] = f.read().splitlines()
        return self.embeddings_dict[category_id].index(filename)
    
    # e.g. "20100408-american-films"
    def load_embeddings(self, file_id, print_filename = True, print_info = True):
        filename = self.embeddings_directory + file_id + ".txt"
        if print_filename:
            print(filename)
        embeddings = numpy.loadtxt(self.embeddings_directory + file_id + ".txt")
        if print_info:
            print(embeddings.shape, type(embeddings))
        return embeddings


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
    
# Example: Read source text
if False:
    print(len(data_accessor.read_source_text(id_british_a, "Monty_Python_s_The_Meaning_of_Life.txt")))
    print()
    
# Example: Look up index
if False:
    print(data_accessor.get_source_text_filename(id_british, 189))
    print()
    
# Example: Look up filename
if False:
    print(data_accessor.get_source_text_index(id_british, "Monty_Python_s_The_Meaning_of_Life.txt"))
    print()
    
# Example: Load embeddings
if False:
    print(data_accessor.load_embeddings(id_british_a).shape);
    print()
