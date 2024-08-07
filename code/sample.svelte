<script>
    import { writable } from 'svelte/store';
  
    // Create a writable store to manage state
    let name = writable('Alice');
    let numbers = writable([1, 2, 3]);
  
    function greet() {
      // Access the store value using $ prefix
      console.log(`Hello, ${$name}!`);
    }
  
    function addNumber() {
      // Update the store value
      numbers.update(n => [...n, n.length + 1]);
    }
</script>
  
<main>
  <h1>Hello World</h1>
  <button on:click={greet}>Greet</button>
  <button on:click={addNumber}>Add Number</button>
  <ul>
    {#each $numbers as n}
      <li>Number: {n}</li>
    {/each}
  </ul>
</main>

<style>
  h1 {
    color: #ff3e00;
  }

  button {
    margin-right: 10px;
  }
</style>
  