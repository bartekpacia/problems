# Circular JSON

**Implement dumpcirc / parsecirc**

Design two helper functions, dump_circ(obj) and parse_circ(text),
that let a developer serialize a Java-Script–style object or array containing circular references to a plain JSON-compatible string,
then restore it back to an equivalent in-memory structure.

Any valid JSON output is acceptable, no particular structure is required.

A circular reference occurs when an object (or array) ends up pointing—directly or indirectly—back to itself;
ordinary `JSON.stringify` / `.loads` would choke on this.
Also implement an `objId` function that returns a unique, stable numeric ID for the lifetime of an object.

### Example 1: simple self-loop

```ts
const a: any[] = [1, 2];
a.push(a); // a → [1, 2, [...]]
const s = dump_circ(a);
const b = parse_circ(s);
console.assert(JSON.stringify(b.slice(0, 2)) === JSON.stringify([1, 2]));
console.assert(b[2] === b); // restored reference
```

### Example 2: Two arrays pointing at each other

```ts
const a: any[] = [1, 2];
const b: any[] = [3, a];
a.push(b); // now a ⟷ b
const txt = dump_circ({ a, b });
const obj = parse_circ(txt);
console.assert(obj.a[2] === obj.b);
console.assert(obj.b[1] === obj.a); // reference maintained
```

### Example 3: Shared array (may be illustrative to think of JSON dump plan)

```ts
const shared: any[] = [42];
const a: any[] = [shared, 1];
const b: any[] = [shared, 2];
const payload = dump_circ([a, b]);
const restored = parse_circ(payload);
console.assert(restored[0][0] === restored[1][0]); // still one shared node
```
