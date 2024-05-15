# テストの考え方と実装方法 in Python

[単体テストの考え方／使い方](https://book.mynavi.jp/ec/products/detail/id=134252)

![書籍表紙](https://book.mynavi.jp/files/topics/134252_ext_06_0.jpg?v=1670578534)

本文書では、**古典学派 (デトロイト学派) の解釈を採用**しています。

- [テストの考え方と実装方法 in Python](#テストの考え方と実装方法-in-python)
  - [テストの種類](#テストの種類)
    - [単体テスト (Unit Test) の概要](#単体テスト-unit-test-の概要)
    - [統合テスト (Integration Test) の概要](#統合テスト-integration-test-の概要)
    - [E2E (End to End Test) の概要](#e2e-end-to-end-test-の概要)
  - [テストを実装する理由](#テストを実装する理由)
  - [プロセス外依存](#プロセス外依存)
    - [管理下にある依存 (managed dependency)](#管理下にある依存-managed-dependency)
    - [管理下にない依存 (unmanaged dependency)](#管理下にない依存-unmanaged-dependency)
  - [テストの品質の維持](#テストの品質の維持)
  - [網羅率](#網羅率)
    - [コード網羅率 (code coverage)](#コード網羅率-code-coverage)
    - [分岐網羅率 (branch coverage)](#分岐網羅率-branch-coverage)
    - [網羅率をテストスイートの品質としてはいけない理由](#網羅率をテストスイートの品質としてはいけない理由)
  - [品質の良いテストスイートの条件](#品質の良いテストスイートの条件)
    - [テストすることが開発サイクルの中に組み込まれている](#テストすることが開発サイクルの中に組み込まれている)
    - [コードベースの特に重要な部分飲みがテスト対象になっている](#コードベースの特に重要な部分飲みがテスト対象になっている)
    - [最小限の保守コストで最大限の価値を生み出すようになっている](#最小限の保守コストで最大限の価値を生み出すようになっている)

## テストの種類

- 単体テスト (Unit Test)
- 統合テスト (Integration Test)
- E2Eテスト (End to End Test)

### 単体テスト (Unit Test) の概要

- **1単位の振る舞い (a unit of behavior)** を検証すること
- 実行時間が短いこと
- 他のテストケースから隔離された状態で実行できること

単体テストでは、関数やクラスのメソッドなど、**1つの振る舞い**を検証します。

また、実行時間を短くすることで、**繰り返し単体テストを実行**できるように開発者の負担を軽減します。
実行時間が長くなると、開発者がテストを実行する回数が減り、バグを見つけるまでの時間が長くなります。
バグが見つかるまでの時間が長くなると、それまでにコードベースは大きくなるため、バグの特定と修正に時間がかかるようになります。

さらに、それぞれの単体テストが他の単体テストと独立することで、他の単体テストからの影響を受けず、個別に実行できるようになります。
これに、単体テストを**個別に実行**したり、同時に**複数の単体テストを並行／並列で実行**することができます。

### 統合テスト (Integration Test) の概要

`統合テスト`は、システム全体が意図したように機能することを検証するテストです。
システムの`ユースケース`ごとに、統合テストを実装して、それぞれまたは連続して実行します。

### E2E (End to End Test) の概要

`E2Eテスト`は、統合テストの上位に位置するテストです。
統合テストでは、システムが依存するメール送信サービスなどの外部サービスをテストダブルに置き換えますが、`E2Eテスト`では、ほぼすべての依存を実際のサービスを使用してテストします。

本文書では、`E2Eテスト`は説明の対象外とします。

## テストを実装する理由

テストを実装する理由は、システムが**将来も持続的に成長できるようにするため**です。
テストが実装されているシステムのことを`テスト対象システム (SUT: System Under Test)`と呼びます。

ほとんどのシステムは、リリース後に何度も仕様変更や改修が行われ、その中で`リファクタリング`されます。
テストが実装されているシステムの仕様変更や改修は、単体／統合テストを実行することで、変更がシステム全体に影響を与えないことを確認できます。
変更によりシステムに不具合が発生することを`退行 (regression)`と呼びますが、SUTは、退行を防ぐことができ、仕様変更や改修に対する開発者の負担を軽減します。

逆に、SUTでないシステムの変更は、変更がシステムに影響を与えたかを確認する工数が多くなり、開発者の負担が大きくなります。
この負担は、開発者のモチベーションを下げ、システムを変更しない理由となり、システムの成長を妨げるようになります。

システムのコードベースは、リリース後に成長しはじめ、劣化する傾向があるため、エントロピー（無秩序の量）が増大するため、リファクタリングが必要になります。
SUTは、退行を生み出す可能性が低くなり、リファクタリングに対する開発者の心理的不安をなくすことができます。

逆に、一時的に作成するプログラムなど、成長することがないシステムに対しては、簡易的なテストの実装で済ましたり、テストの実装を省くことができると考えられます。

![プロジェクトの成長](./images/project-growth.png)

## プロセス外依存

システムは、データベースやメール配信サービスなど、システムが動作するプロセス以外で動作する依存があります。
この`プロセス外依存`は、次の2つに区分されます。

- 管理下にある依存 (managed dependency)
- 管理下にない依存 (unmanaged dependency)

### 管理下にある依存 (managed dependency)

`管理下にある依存`は、SUTしかアクセスしないデータベースなど、SUTが自由に操作でき、その振る舞いを確認できる依存を示します。

単体テストでは、管理下にある依存をテストダブルで置き換え、テストの実行時間を短くします。
一方、統合テストでは、管理下にある依存を実際に利用したテストを実装します。

### 管理下にない依存 (unmanaged dependency)

`管理下にない依存`は、外部サービスなど、費用や過度に負荷を与えることができないなどの理由でSUTが自由に操作できない依存を示します。
管理下にない依存は、単体テスト及び統合テストでテストダブルに置き換えます。

## テストの品質の維持

テストの品質が悪いとは次の状態を指します。

- エラーが発生してテストを実行できない
- 偽陽性 (False Positive) が発生する
  - プロダクションコードが正しいにも関わらず、テストに失敗する
- 偽陰性 (False Negative) が発生する
  - プロダクションコードが誤っているにも関わらず、テストに成功する

テストの品質が悪いとテストが信頼されなくなり、テストが実行されません。
その結果、システムの持続的な成長が阻害されます。

よって、テストの品質を保つために次を心がける必要があります。

- プロダクションコードのリファクタリングに合わせて、テストをリファクタリングする。
- プロダクションコードを変更するたびにテストを実行する。
- テストが偽陽性や偽陰性を発生した場合は、修正する。

プロダクションコードがどのように振る舞うか理解するために、テストコードのリーディングは非常に有益です。
よって、プロダクションコードだけでなくテストコードも適切に保守する必要があります。

## 網羅率

テストスイート（テスト全体）の品質を評価する指標として`網羅率`があります。
テストスイートの品質は、必ずしも**網羅率から判断できない**ことに注意してください。

網羅率には次の2つがあります。

- `コード網羅率 (code coverage)`
- `分岐網羅率 (branch coverage)`

### コード網羅率 (code coverage)

`コード網羅率`は、テストスイートがプロダクションコードの行をどれだけ実行したかで計算されます。

$コード網羅率 = \frac{テストスイートが実行した行数}{プロダクションコードの行数}$

次の`is_string_long`関数のコード網羅率を考えます。

```python
def is_string_long(s: str) -> bool:   # 1
    if len(s) > 5:                    # 2
        return True                   # 3
    return False                      # 4

import unittest
class TestIsStringLong(unittest.TestCase):
    def test_is_string_long(self):
        result = is_string_long("abc")
        self.assertFalse(result)
```

上記の場合、`len(s)`は`3`であるため、1, 3, 4行目が実行され、コード網羅率は0.75 (3 / 4)になります。

しかし、`is_string_long`関数を次に変更したとき、コード網羅率は1.0になります。
プロダクションコードのリファクタリングによりテストの品質は向上していませんが、コード網羅率は0.75から1.0に向上しました。

```python
def is_string_long(s: str) -> bool:
    return True if len(s) > 5 else False
```

**コード網羅率はプロダクションコードの実装方法で結果が変わる**ため、コード網羅率だけでテストスイートの品質を判断することはできません。

### 分岐網羅率 (branch coverage)

`分岐網羅率`は、テストスイートがプロダクションコードに存在する分岐した経路を、どれだけ実行したかで計算されます。

$分岐網羅率 = \frac{テストスイートが実行した分岐数}{プロダクションコードの分岐数}$

リファクタリング前後の`is_string_long`関数の分岐網羅率はどちらも0.5です。

ここで、次のような関数の結果を評価しない**邪悪な**`確認不在のテスト`を実装すると、分岐網羅率は1.0になります。

```python
class TestIsStringLong(unittest.TestCase):
    def test_is_string_short(self):
        result = is_string_long("abc")

    def test_is_string_long(self):
        result = is_string_long("abcdef")
```

上記のテストは、`is_string_long`関数の分岐をすべて実行していますが、関数の結果である`result`を評価していません。

### 網羅率をテストスイートの品質としてはいけない理由

網羅率をテストスイートの品質としてはいけない理由は次の通りです。

- プロダクションコードの実装方法によってコード網羅率が変わる
- 分岐網羅率を増やすために、確認不在のテストが実装される

**網羅率でテストスイートの品質が悪いことを評価できます**。
しかし、逆に**網羅率はテストスイートの品質が良いことを評価できません**。

コード網羅率または分岐網羅率が0.6などの場合、テストされていないプロダクションコードが多く残っていることを示し、これはテストスイートの品質が悪いことを示します。

基本的に網羅率を高く維持されていれば、**テストされている**とみなせます。
しかし、網羅率を例えば85%以上に維持するなど、数値目標を設定することは、開発者に**人工的な目標**を設定することになり、テストスイートの品質を向上させることに繋がりません。

## 品質の良いテストスイートの条件

- テストすることが開発サイクルの中に組み込まれている
- コードベースの特に重要な部分のみがテスト対象になっている
- 最小限の保守コストで最大限の価値を生み出している

### テストすることが開発サイクルの中に組み込まれている

テストは常に実行されなければならず、テストの実行が開発サイクルの中に組み込まれていなくてはなりません。
理想的には、仮に変更が些細なことであっても、コードに変更を加えるたびにテストが実施されるようになっていることです。

リモートリポジトリの`develop`または`main`ブランチにプッシュされるたびに、CI/CDパイプラインが実行されるように設定することが望ましいです。

### コードベースの特に重要な部分飲みがテスト対象になっている

ほとんどのシステムにおいて、システムの核はビジネスロジックを含むコードで、それらは**ドメイン**または**ドメインモデル**と呼ばれます。
テストの実装及び実行に費やした時間が価値として効果的に得られるのは、ドメインに対するテストです。

逆に価値の低いコードには、次などが挙げられます。

- インフラに関するコード
- フレームワーク、ライブラリ、データベースまたは外部サービスなど依存関係に関するコード
- インターフェイスなど、構成要素同士を結びつけるコード

ドメインをテストしやすくするために、**ドメインは価値の低いコードと分離**する（関係を持たない）必要があります。

### 最小限の保守コストで最大限の価値を生み出すようになっている

単体テストにおいて、最小限の保守コストで最大限の価値を生み出すことは非常に難しいです。
これをできるようにするためには、次ができなくてはなりません。

- 価値のあるテストケースを認識できること
  - 逆に、価値の低いテストケースを認識できること
- 価値のあるテストケースを作成できること
