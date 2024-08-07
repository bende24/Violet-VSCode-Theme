<template>
    <div id="app">
        <h1>{{ title }}</h1>
        <button @click="greet">Greet</button>
        <ul>
            <li v-for="n in numbers" :key="n">Number: {{ n }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: 'Hello World',
            name: 'Alice',
            numbers: [1, 2, 3],
        };
    },
    methods: {
        greet() {
            console.log(`Hello, ${this.name}!`);
        }
    }
};
</script>

<style scoped>
h1 {
    color: #42b983;
}
</style>