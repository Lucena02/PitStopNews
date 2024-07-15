<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
  news: {
    title: string;
    description: string;
    urlToImage: string;
  };
}>();

console.log(props.news.title);
console.log(props);
</script>

<template>

    <div class="caixa">
        <div class="imagem">
            <img class="imagemMesmo" :src="props.news.urlToImage || './../assets/noImageTemplate.jpg'" />
        </div>
        <div class="resto">
            <div class="headline">
                {{ props.news.title || "No Title" }}
            </div>
            <div class="description">
                {{ props.news.description || "No Description" }}
            </div>
        </div>

    </div>
</template>


<style>
.caixa{
    display: flex;
    background-color: var(--backgroundBox);
    width: 35vw;
    height: 15vh;
    min-height: 100px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 2px 2px 2px 2px rgba(0, 0, 0, 0.2);
}

.imagem{
    display: flex;
    flex:1;
    justify-content: center;
    align-items: center;
}

.imagemMesmo{
    border-radius: 15px;
    width: 90%;
    height: 90%;

}

.resto{
    margin-left:20px;
    font-family: Arial;
    color: var(--fontColor);
    flex:3;
}

.headline{
    margin-top: 15px;
    font-weight: bold;
    font-size: 24px;
}

.description{

}

@media  (max-width: 800px) {
    .caixa{
        width: 80vw;
    }

}

</style>
