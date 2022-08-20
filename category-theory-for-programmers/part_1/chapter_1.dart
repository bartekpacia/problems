int multiplier(int a) {
  return a * 3;
}

String concat(String s) {
  return s + ' Fuzz';
}

void main() {
  expect(1, id(1));
  expect('x', id('x'));

  expect(
    compose(
      f: () => multiplier(3),
      g: multiplier,
    ),
    27,
  );

  expect(
    compose(
      f: () => concat('Bartek'),
      g: concat,
    ),
    'Bartek Fuzz Fuzz',
  );
}

void expect(dynamic a, dynamic b) {
  if (a != b) {
    throw Exception("$a != $b");
  }
}

/// The identity function.
T id<T>(T x) {
  return x;
}

/// The composition function.
C compose<B, C>({
  required B Function() f,
  required C Function(B b) g,
}) {
  return g(f());
}
