import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useBalanceStore = defineStore("balance", () => {
  const balances = ref([
    {
      name: "김하나",
      balance: 100000,
    },
    {
      name: "김두리",
      balance: 10000,
    },
    {
      name: "김서이",
      balance: 100,
    },
  ]);
  const selectedBalance = function (selectedName) {
    const selected = balances.value.find(
      (balance) => balance.name === selectedName
    );
    return selected;
  };

  return { balances, selectedBalance };
});
