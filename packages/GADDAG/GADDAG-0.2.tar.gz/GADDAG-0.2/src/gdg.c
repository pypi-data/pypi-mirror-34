#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#include "gdg.h"

uint8_t ch_to_idx(char ch) {
    ch = tolower(ch);
    if (ch == '+') return 0;
    else if (ch >= 97 && ch <= 122) return ch - 96;
    else {
        fprintf(stderr, "Invalid character '%c'\n", ch);
        exit(EXIT_FAILURE);
    }
}

char idx_to_ch(uint8_t idx) {
    if (idx == 0) return '+';
    else if (idx >= 1 && idx <= 27) return idx + 96;
    else {
        fprintf(stderr, "Invalid index '%d'\n", idx);
        exit(EXIT_FAILURE);
    }
}

Result newResult(char *str, Result next) {
    Result self = (Result)malloc(sizeof(struct Result_Struct));
    if (self == NULL) {
        fprintf(stderr, "Failed to create result, out of memory.\n");
        exit(EXIT_FAILURE);
    }

    if (next) next->prev = self;

    self->str = strdup(str);
    if (self->str == NULL) {
        fprintf(stderr, "Failed to duplicate string, out of memory.\n");
        exit(EXIT_FAILURE);
    }
    self->next = next;
    self->prev = NULL;


    return self;
}

void grow_GADDAG(GADDAG gdg) {
    unsigned int old_cap = gdg->cap;
    unsigned int new_cap = old_cap + DEFAULT_CAP;
    gdg->cap = new_cap;

    gdg->edges = realloc(gdg->edges, new_cap * MAX_CHARS * sizeof(unsigned int));
    if (gdg->edges == NULL) {
        fprintf(stderr, "Failed to grow the GADDAG, out of memory.\n");
        exit(EXIT_FAILURE);
    }
    memset(gdg->edges + old_cap * MAX_CHARS, 0, (new_cap - old_cap) * MAX_CHARS * sizeof(unsigned int));

    gdg->letter_sets = realloc(gdg->letter_sets, new_cap * sizeof(unsigned int));
    if (gdg->letter_sets == NULL) {
        fprintf(stderr, "Failed to grow the GADDAG, out of memory.\n");
        exit(EXIT_FAILURE);
    }
    memset(gdg->letter_sets + old_cap, 0, (new_cap - old_cap) * sizeof(unsigned int));
}

unsigned int follow_edge(GADDAG gdg, unsigned int node, char ch) {
    uint8_t ch_idx = ch_to_idx(ch);
    return gdg->edges[node * MAX_CHARS + ch_idx];
}

void set_edge(GADDAG gdg, unsigned int node, char ch, unsigned int dst) {
    uint8_t ch_idx = ch_to_idx(ch);
    gdg->edges[node * MAX_CHARS + ch_idx] = dst;
    gdg->num_edges++;
}

unsigned int add_edge(GADDAG gdg, unsigned int node, char ch) {
    unsigned int dst = follow_edge(gdg, node, ch);
    if (dst == 0) {
        dst = gdg->num_nodes++;
        if (gdg->num_nodes >= gdg->cap) grow_GADDAG(gdg);
        set_edge(gdg, node, ch, dst);
    }
    return dst;
}

void add_end(GADDAG gdg, unsigned int node, char ch) {
    uint8_t ch_idx = ch_to_idx(ch);
    gdg->letter_sets[node] |= (1 << ch_idx);
}

unsigned int add_final_edge(GADDAG gdg, unsigned int node, char ch, char end_ch) {
    unsigned int dst = add_edge(gdg, node, ch);
    add_end(gdg, dst, end_ch);
    return dst;
}

void force_edge(GADDAG gdg, unsigned int node, char ch, unsigned int dst) {
    unsigned int next_node = follow_edge(gdg, node, ch);
    if (next_node != dst) {
        if (next_node != 0) {
            fprintf(stderr, "Edge already exists for forced edge\n");
            exit(EXIT_FAILURE);
        }
        set_edge(gdg, node, ch, dst);
    }
}

Result _crawl(GADDAG gdg, unsigned int node, char *partial_word, bool wrapped, Result res) {
    size_t len = strlen(partial_word);
    unsigned int letter_set = gdg->letter_sets[node];
    char ch;
    unsigned int next_node;
    char *word;
    char *new_partial_word;
    uint8_t start_idx;

    if (wrapped) start_idx = 1;
    else start_idx = 0;

    for (unsigned int i = start_idx; i < MAX_CHARS; ++i) {
        ch = idx_to_ch(i);

        if (i > 0 && (letter_set >> i) & 1) {
            word = malloc(len + 2);
            if (word == NULL) {
                fprintf(stderr, "Failed to allocate 'word', out of memory.\n");
                exit(EXIT_FAILURE);
            }
            
            if (wrapped) {
                strcpy(word, partial_word);
                word[len] = ch;
                word[len + 1] = '\0';
            } else {
                word[0] = ch;
                strcpy(word + 1, partial_word);
            }
            
            if (!res) res = newResult(word, NULL);
            else res = newResult(word, res);
            free(word);
        }


        next_node = follow_edge(gdg, node, ch);
        if (next_node) {
            if (i == 0) res = _crawl(gdg, next_node, partial_word, 1, res);
            else {
                new_partial_word = malloc(len + 2);
                if (new_partial_word == NULL) {
                    fprintf(stderr, "Failed to allocate 'new_partial_word', out of memory.\n");
                    exit(EXIT_FAILURE);
                }

                if (wrapped) {
                    strcpy(new_partial_word, partial_word);
                    new_partial_word[len] = ch;
                    new_partial_word[len + 1] = '\0';
                } else {
                    new_partial_word[0] = ch;
                    strcpy(new_partial_word + 1, partial_word);
                }

                res = _crawl(gdg, next_node, new_partial_word, wrapped, res);
                free(new_partial_word);
            }
        }
    }

    return res;
}

Result _crawl_end(GADDAG gdg, unsigned int node, char *partial_word, Result res) {
    size_t len = strlen(partial_word);
    unsigned int letter_set = gdg->letter_sets[node];
    char ch;
    unsigned int next_node;
    char *word;
    char *new_partial_word;

    for (unsigned int i = 1; i < MAX_CHARS; ++i) {
        ch = idx_to_ch(i);

        if ((letter_set >> i) & 1) {
            word = malloc(len + 2);
            if (word == NULL) {
                fprintf(stderr, "Failed to allocate 'word', out of memory.\n");
                exit(EXIT_FAILURE);
            }
            word[0] = ch;
            strcpy(word + 1, partial_word);
            
            if (!res) res = newResult(word, NULL);
            else res = newResult(word, res);
            free(word);
        }

        next_node = follow_edge(gdg, node, ch);
        if (next_node) {
            new_partial_word = malloc(len + 2);
            if (new_partial_word == NULL) {
                fprintf(stderr, "Failed to allocate 'new_partial_word', out of memory.\n");
                exit(EXIT_FAILURE);
            }
            new_partial_word[0] = ch;
            strcpy(new_partial_word + 1, partial_word);

            res = _crawl_end(gdg, next_node, new_partial_word, res);
            free(new_partial_word);
        }
    }

    return res;
}

