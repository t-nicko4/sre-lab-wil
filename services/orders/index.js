
import express from "express";
const app = express();
const PORT = process.env.PORT || 8001;

const orders = [
  { id: 101, userId: 1, item: "Keyboard" },
  { id: 102, userId: 2, item: "Mouse" }
];

app.get("/health", (_req, res) => res.json({ status: "ok" }));
app.get("/orders", (_req, res) => res.json(orders));

app.listen(PORT, () => console.log(`orders-service listening on ${PORT}`));