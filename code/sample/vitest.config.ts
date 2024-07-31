import { defineConfig } from "vitest/config";

export default defineConfig({
    test: {
        globals: true,
        environment: "node", // You can use 'jsdom' if you need browser-like environment
    },
});
