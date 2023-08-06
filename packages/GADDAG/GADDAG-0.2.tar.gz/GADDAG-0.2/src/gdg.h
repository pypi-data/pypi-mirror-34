#ifndef GDG_H_INCLUDED
#define GDG_H_INCLUDED
#include "cgaddag.h"

Result newResult(char *str, Result next);

uint8_t ch_to_idx(char ch);
char idx_to_ch(uint8_t idx);

unsigned int follow_edge(GADDAG gdg, unsigned int node, char ch);
void set_edge(GADDAG gdg, unsigned int node, char ch, unsigned int dst);
unsigned int add_edge(GADDAG gdg, unsigned int node, char ch);
void add_end(GADDAG gdg, unsigned int node, char ch);
unsigned int add_final_edge(GADDAG gdg, unsigned int node, char ch, char end_ch);
void force_edge(GADDAG gdg, unsigned int node, char ch, unsigned int force_node);

Result _crawl(GADDAG gdg, unsigned int st, char *partial_word, bool wrapped, Result res);
Result _crawl_end(GADDAG gdg, unsigned int st, char *partial_word, Result res);
#endif
