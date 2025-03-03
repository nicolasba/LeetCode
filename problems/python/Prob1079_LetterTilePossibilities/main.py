class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        set_seqs = set()

        # Iterate through all possible sequence of variations of 
        # of particular length and add them to set.
        for i in range(1, len(tiles) + 1):
            self.recIteratePossibleSequences(tiles, i, "", set_seqs)

        # Will get rid of duplicates
        return len(set_seqs)

    def recIteratePossibleSequences(self, avail_tiles, seq_length, acc, set_seqs):
        if len(acc) >= seq_length:
            set_seqs.add(acc)
            return

        for i, tile in enumerate(avail_tiles):
            self.recIteratePossibleSequences(avail_tiles[:i] + avail_tiles[i+1:], seq_length, acc + tile, set_seqs)
