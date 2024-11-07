<template>
  <div>
    <h2>보유 명함 목록</h2>
    <div class="card-container">
      <BusinessCardDetail
        v-for="card in businessCards"
        :key="card.name"
        :card="card"
        @delete-card-event="deleteCard(card)"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import BusinessCardDetail from "@/components/BusinessCardDetail.vue";

const businessCards = ref([
  { name: "일론 머스크", title: "테슬라 테크노킹" },
  { name: "래리 엘리슨", title: "오라클 창업주" },
  { name: "빌 게이츠", title: "마이크로소프트 공동창업주" },
  { name: "래리 페이지", title: "구글 공동창업주" },
  { name: "세르게이 브린", title: "구글 공동창업주" },
]);

const deleteCard = function (item) {
  // 1. idx 찾아서 splice 하는 방법
  // const idx = item.value.findIndex(
  //   (c) => c.name === item.name
  // );
  // if (idx !== -1) {
  //   businessCards.value.splice(idx, 1);
  // }

  // 2. filter로 객체 비교해서 새로운 배열 생성
  // 이게 더 간단하네!
  businessCards.value = businessCards.value.filter(
    (businesscard) => businesscard != item
  );
};
</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
