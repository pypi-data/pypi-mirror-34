#ifndef GADDAG_H_INCLUDED
#define GADDAG_H_INCLUDED
extern unsigned int MAX_CHARS;
extern unsigned int DEFAULT_CAP;

typedef struct Result_Struct* Result;
typedef struct GADDAG_Struct* GADDAG;

struct Result_Struct {
    char* str;
    Result next;
    Result prev;
};

struct GADDAG_Struct {
    unsigned int *edges;
    unsigned int *letter_sets;
    unsigned int cap;
    unsigned int num_words;
    unsigned int num_nodes;
    unsigned int num_edges;
};

void destroy_result(Result res);

GADDAG newGADDAG(void);
void destroy_GADDAG(GADDAG gdg);
void add_word(GADDAG gdg, char *word);
bool has(GADDAG gdg, char *word);
Result starts_with(GADDAG gdg, char *prefix);
Result contains(GADDAG gdg, char *sub);
Result ends_with(GADDAG gdg, char *suffix);
void edges(GADDAG gdg, unsigned int node, char *buffer);
void letter_set(GADDAG gdg, unsigned int node, char *buffer);
bool is_end(GADDAG gdg, unsigned int node, char ch);
unsigned int follow_edge(GADDAG gdg, unsigned int node, char ch);
#endif
