class Solution {
    public String[] findRelativeRanks(int[] score) {
        Map<Integer, Integer> scoreMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < score.length; i++) {
            scoreMap.put(score[i], i);
        }

        Arrays.sort(score);
        String results[] = new String[score.length];

        for (int i = score.length - 1; i >= 0; i--) {
            int rank = score.length - i;

            if (rank == 1) {
                results[scoreMap.get(score[i])] = "Gold Medal";
            } else if (rank == 2) {
                results[scoreMap.get(score[i])] = "Silver Medal";
            } else if (rank == 3) {
                results[scoreMap.get(score[i])] = "Bronze Medal";
            } else {
                results[scoreMap.get(score[i])] = String.valueOf(rank);
            }
        }

        return results;
    }
}