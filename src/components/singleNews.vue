<script setup lang="ts">


</script>

<template>

    <div class="caixa">
        <div class="imagem">
            <img class="imagemMesmo"src="./../assets/noImageTemplate.jpg">
        </div>
        <div class="resto">
            <div class="headline">
                Esta notícia é um teste!!!
            </div>
            <div class="description">
                Isto é a descrição da notícia, yappingyapping
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
