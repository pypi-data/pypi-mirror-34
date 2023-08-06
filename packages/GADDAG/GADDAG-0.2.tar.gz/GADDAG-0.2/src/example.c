#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cgaddag.h"

int main() {
    GADDAG gdg = newGADDAG();

    /* FILE *fp = fopen("sowpods.txt", "r"); */
    /* char *line = NULL; */
    /* size_t len = 0; */
    /* ssize_t read; */

    /* if (fp == NULL) exit(EXIT_FAILURE); */

    /* while ((read = getline(&line, &len, fp)) != -1) { */
    /*     line[strcspn(line, "\n")] = '\0'; */
    /*     add_word(gdg, line); */
    /* } */

    /* fclose(fp); */

    add_word(gdg, "CARE");
    add_word(gdg, "CAR");
    add_word(gdg, "BAR");
    
    printf("Words in GADDAG: %u\n", gdg->num_words);
    printf("Total nodes: %u\n", gdg->num_nodes);
    printf("Total edges: %u\n", gdg->num_edges);

    printf("\n");
    printf("CARE in gdg: %d\n", has(gdg, "CARE"));
    printf("CAR in gdg: %d\n", has(gdg, "CAR"));
    printf("FOO in gdg: %d\n", has(gdg, "FOO"));

    unsigned int r_st = follow_edge(gdg, 0, 'R');
    unsigned int ra_st = follow_edge(gdg, r_st, 'A');

    char edge_letters[MAX_CHARS];
    memset(edge_letters, '\0', MAX_CHARS);
    edges(gdg, 0, edge_letters);
    printf("\nEdges from root: %s\n", edge_letters);

    char end_letters[MAX_CHARS];
    memset(end_letters, '\0', MAX_CHARS);
    letter_set(gdg, ra_st, end_letters);
    printf("Letter set for root -> R -> A: %s\n", end_letters);

    Result res;
    Result tmp;

    printf("\nFinding words ending with 'PAR'\n");
    res = ends_with(gdg, "par");
    if (res) {
        tmp = res;
        while (tmp) {
            printf("  %s\n", tmp->str);
            tmp = tmp->next;
        }
        destroy_result(res);
    } else printf("  No words found\n");

    printf("\nFinding words starting with 'CARB'\n");
    res = starts_with(gdg, "carb");
    if (res) {
        tmp = res;
        while (tmp) {
            printf("  %s\n", tmp->str);
            tmp = tmp->next;
        }
        destroy_result(res);
    } else printf("  No words found\n");

    printf("\nFinding words containing 'DROP'\n");
    res = contains(gdg, "drop");
    if (res) {
        tmp = res;
        while (tmp) {
            printf("  %s\n", tmp->str);
            tmp = tmp->next;
        }
        destroy_result(res);
    } else printf("  No words found\n");

    destroy_GADDAG(gdg);
}

