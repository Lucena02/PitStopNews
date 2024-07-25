<script setup lang="ts">
import { defineProps } from 'vue';
import { SquareArrowOutUpRight } from 'lucide-vue-next';

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
        <div class="d1">
          Source:
          {{ props.source || "No Source" }}
        </div>
        <div class="d2">
          <a :href="props.link" >
            <SquareArrowOutUpRight class="iconRedirect"/>
          </a>
          
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.iconRedirect{
  color: var(--fontColor);
  height:18px;
}
.caixa {
  display: flex;
  background-color: var(--backgroundBox);
  width: 40vw;
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
  flex:6;
  display:flex;
  margin-top: 15px;
  font-weight: bold;
  font-size: 20px;
  overflow: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--fontColor) var(--backgroundBox);
}


.description {
  flex:1;
  display: flex;
  margin-top: auto;
  margin-bottom: 10px;
  margin-top: 10px;
}

.d2 {
  margin-left: auto;
  margin-right: 10px;
}

@media (max-width: 800px) {
  .caixa {
    width: 80vw;
  }
}
</style>
