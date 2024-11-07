<template>
  <div class="card">
    <h4>이름: {{ card.name }}</h4>
    <p>직함: {{ card.title }}</p>
    <button @click="deleteCardFunc(card)">명함 삭제</button>

    <!-- props 변수에 할당했을 경우 -->
    <!-- <button @click="deleteCardFunc">명함 삭제</button> -->
  </div>
</template>

<script setup>
// const props = defineProps({
//   card: Object,
// });

// const emit = defineEmits(["deleteCardEvent"]);
// const deleteCardFunc = function () {
//   emit("deleteCardEvent", props.card);
// };

defineProps({
  card: Object,
});

const emit = defineEmits(["delete-card-event"]);
const deleteCardFunc = function (card) {
  emit("delete-card-event", card);
};
</script>

<style scoped>
.card {
  /* border: 1px solid gray; */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  background-color: lightgray;
  margin: 10px;
  width: 300px;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
