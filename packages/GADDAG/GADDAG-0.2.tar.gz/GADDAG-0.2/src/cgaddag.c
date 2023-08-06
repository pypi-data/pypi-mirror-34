#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "gdg.h"

unsigned int MAX_CHARS = 27;
unsigned int DEFAULT_CAP = 100;

GADDAG newGADDAG() {
    GADDAG gdg = (GADDAG)malloc(sizeof(struct GADDAG_Struct));

    gdg->cap = DEFAULT_CAP;
    gdg->edges = calloc(MAX_CHARS * gdg->cap, sizeof(unsigned int));
    gdg->letter_sets = calloc(gdg->cap, sizeof(unsigned int));
    gdg->num_words = 0;
    gdg->num_nodes = 1;
    gdg->num_edges = 0;

    return gdg;
}

void add_word(GADDAG gdg, char *word) {
    size_t l = strlen(word);

    gdg->num_words++;

    // Add path from last letter in word
    unsigned int node = 0;
    for (int i = l - 1; i >= 2; --i) {
        node = add_edge(gdg, node, word[i]);
    }
    node = add_final_edge(gdg, node, word[1], word[0]);

    if (l == 1) return;

    // Add path from penultimate letter in word
    node = 0;
    for (int i = l - 2; i >= 0; --i) {
        node = add_edge(gdg, node, word[i]);
    }
    node = add_final_edge(gdg, node, '+', word[l - 1]);

    // Create remaining paths
    for (int m = l - 3; m >= 0; --m) {
        unsigned int force_node = node;
        node = 0;
        for (int i = m; i >= 0; --i) {
            node = add_edge(gdg, node, word[i]);
        }
        node = add_edge(gdg, node, '+');
        force_edge(gdg, node, word[m + 1], force_node);
    }
}

void letter_set(GADDAG gdg, unsigned int node, char *buffer) {
    uint8_t offset = 1;
    uint8_t i = 0;
    while (offset < MAX_CHARS) {
        if ((gdg->letter_sets[node] >> offset) & 1) {
            buffer[i++] = idx_to_ch(offset);
        }
        offset++;
    }
}

void edges(GADDAG gdg, unsigned int node, char *buffer) {
    uint8_t offset = 0;
    uint8_t i = 0;
    unsigned int next_node;
    char ch;

    while (offset < MAX_CHARS) {
        ch = idx_to_ch(offset);
        next_node = follow_edge(gdg, node, ch);
        if (next_node) buffer[i++] = ch;
        offset++;
    }
}

bool is_end(GADDAG gdg, unsigned int node, char ch) {
    uint8_t ch_idx = ch_to_idx(ch);
    return gdg->letter_sets[node] & (1 << ch_idx);
}

bool has(GADDAG gdg, char *word) {
    size_t l = strlen(word);

    unsigned int node = 0;
    for (int i = l - 1; i > 0; --i) {
        node = follow_edge(gdg, node, word[i]);
        if (!node) return false;
    }

    return is_end(gdg, node, word[0]);
}

Result starts_with(GADDAG gdg, char *prefix) {
    size_t l = strlen(prefix);
    Result res = NULL;
    unsigned int node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && is_end(gdg, node, prefix[i])) {
            res = newResult(prefix, NULL);
        }
        node = follow_edge(gdg, node, prefix[i]);
        if (!node) return NULL;
    }

    node = follow_edge(gdg, node, '+');
    if (!node) return NULL;

    return _crawl(gdg, node, prefix, 1, res);
}

Result contains(GADDAG gdg, char *sub) {
    size_t l = strlen(sub);
    Result res = NULL;
    unsigned int node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && is_end(gdg, node, sub[i])) {
            res = newResult(sub, NULL);
        }
        node = follow_edge(gdg, node, sub[i]);
        if (!node) return NULL;
    }

    return _crawl(gdg, node, sub, 0, res);
}

Result ends_with(GADDAG gdg, char *suffix) {
    size_t l = strlen(suffix);
    Result res = NULL;
    unsigned int node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && is_end(gdg, node, suffix[i])) {
            res = newResult(suffix, NULL);
        }
        node = follow_edge(gdg, node, suffix[i]);
        if (!node) return NULL;
    }

    return _crawl_end(gdg, node, suffix, res);
}

void destroy_GADDAG(GADDAG gdg) {
    free(gdg->edges);
    free(gdg->letter_sets);
    free(gdg);
}

void destroy_result(Result res) {
    Result last;
    while (res) {
        last = res;
        res = res->next;
    }

    Result prev;
    while (last) {
        prev = last->prev;
        free(last->str);
        free(last);
        last = prev;
    }
}

