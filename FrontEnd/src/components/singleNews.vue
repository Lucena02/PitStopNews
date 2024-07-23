<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
    title: string;
    image: string;
    link: string;
    source: string;
}>();

console.log(props.title);
console.log(props);
</script>

<template>
  <div class="caixa">
    <div class="imagem">
      <img class="imagemMesmo" :src="props.image || './../assets/noImageTemplate.jpg'" />
    </div>
    <div class="resto">
      <div class="headline">
        {{ props.title || "No Title" }}
      </div>
      <div class="description">
        Source:
        {{ props.source || "No Source" }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.caixa {
  display: flex;
  background-color: var(--backgroundBox);
  width: 35vw;
  height: 15vh;
  min-height: 100px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 2px 2px 2px 2px rgba(0, 0, 0, 0.2);
}

.imagem {
  display: flex;
  flex: 4;
  justify-content: center;
  align-items: center;
}

.imagemMesmo {
  border-radius: 8px;
  width: 94%;
  height: 90%;
}

.resto {
  display: flex;
  flex-direction: column; /* Arrange children in a column */
  margin-left: 10px;
  font-family: Arial;
  color: var(--fontColor);
  flex: 8;
}

.headline {
  margin-top: 15px;
  font-weight: bold;
  font-size: 20px;
}

.description {
  margin-top: auto;
  margin-bottom: 10px;
}

@media (max-width: 800px) {
  .caixa {
    width: 80vw;
  }
}
</style>
