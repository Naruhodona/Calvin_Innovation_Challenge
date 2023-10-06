# !pip install jaro-winkler
# !pip install --upgrade pip
from jaro import jaro_winkler_metric
from numpy import int64, float64

class Test:
    def __init__(self, shape, column_names, datatypes, empty_columns, empty_rows, statistical_descriptive):
        self.correct_ans = 0
        self.wrong_ans = 0
        self.shape = shape
        self.column_names = column_names
        self.datatypes = datatypes 
        self.empty_columns = empty_columns
        self.empty_rows = empty_rows
        self.statistical_descriptive = statistical_descriptive

    def df_shape_test(self):
        try:
            assert self.shape[0] == 129971
            self.correct_ans+=1
        except AssertionError as e:
            print(e)
            print("Jumlah Row Salah!")
            self.wrong_ans +=1

        try:
            assert self.shape[1] == 13
            self.correct_ans+=1
        except AssertionError as e:
            print(e)
            print("Jumlah Kolom Salah!")
            self.wrong_ans +=1

    def df_column_names_test(self):
        try:
            assert self.column_names.tolist() == ['country', 'description', 'designation', 'points', 'price', 'province',
       'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title',
       'variety', 'winery']
            self.correct_ans+=1
        except AssertionError as e:
            print(e)
            self.wrong_ans +=1
            print("Nama Kolom Tidak Sesuai!")

    def df_datatypes_test(self):
        expected_datatypes = {
        'country': object,
        'description': object,
        'designation': object,
        'points': int64,
        'price': float64,
        'province': object,
        'region_1': object,
        'region_2': object,
        'taster_name': object,
        'taster_twitter_handle': object,
        'title': object,
        'variety': object,
        'winery': object
        }
        try:
            for column, expected_type in expected_datatypes.items():
                assert wine_df_datatypes[column] == expected_type, f"Tipe Data Tidak Sesuai Untuk Kolom '{column}'"
            self.correct_ans+=1
        except AssertionError as e:
            print(e)
            self.wrong_ans +=1
            print("Datatypes Tidak Sesuai!")

    def df_null_columns_test(self):
        try:
            empty_columns = self.empty_columns.tolist()
            assert len(empty_columns) == 9
            self.correct_ans+=1
            assert empty_columns == ['country', 'designation', 'price', 'province', 'region_1', 'region_2',
       'taster_name', 'taster_twitter_handle', 'variety']
            self.correct_ans+=1
        except AssertionError as e:
            self.wrong_ans +=1
            print(e)
            print("Nama Kolom yang Memiliki Data Null Tidak Sesuai!")

    def df_empty_rows_test(self):
        try:
            assert self.empty_rows == 204752
            self.correct_ans+=1
        except AssertionError as e:
            print(e)
            self.wrong_ans +=1
            print("Jumlah data yang kosong salah!")

    def df_statistical_descriptive_test(self):
        def find_string_similarity(string1: str, string2: str): return round(jaro_winkler_metric(string1,string2),2)
        test_string = """
        Statistik Deskriptif points untuk keseluruhan Dataframe
        Rata-rata jumlah poin : 88.42
        Nilai Minimum : 80
        Quartil 1 (Q1) : 86.0
        Median (Q2): 88.0
        Quartil 3 (Q3) : 91.0
        Nilai Maksimum : 100
        Standar Deviasi : 3.04

        Statistik Deskriptif points untuk negara US
        Rata-rata jumlah poin : 88.57
        Nilai Minimum : 80
        Quartil 1 (Q1) : 86.0
        Median (Q2): 88.0
        Quartil 3 (Q3) : 91.0
        Nilai Maksimum : 100
        Standar Deviasi : 3.04

        Statistik Deskriptif points untuk negara France
        Rata-rata jumlah poin : 88.73
        Nilai Minimum : 80
        Quartil 1 (Q1) : 87.0
        Median (Q2): 88.0
        Quartil 3 (Q3) : 91.0
        Nilai Maksimum : 100
        Standar Deviasi : 3.04

        Statistik Deskriptif points untuk negara Italy
        Rata-rata jumlah poin : 88.62
        Nilai Minimum : 80
        Quartil 1 (Q1) : 87.0
        Median (Q2): 88.0
        Quartil 3 (Q3) : 90.0
        Nilai Maksimum : 100
        Standar Deviasi : 3.04

        Statistik Deskriptif price untuk keseluruhan Dataframe
        Rata-rata jumlah poin : 35.36
        Nilai Minimum : 4.0
        Quartil 1 (Q1) : 17.0
        Median (Q2): 25.0
        Quartil 3 (Q3) : 42.0
        Nilai Maksimum : 3300.0
        Standar Deviasi : 41.02

        Statistik Deskriptif price untuk negara US
        Rata-rata jumlah poin : 36.57
        Nilai Minimum : 4.0
        Quartil 1 (Q1) : 20.0
        Median (Q2): 30.0
        Quartil 3 (Q3) : 45.0
        Nilai Maksimum : 2013.0
        Standar Deviasi : 41.02

        Statistik Deskriptif price untuk negara France
        Rata-rata jumlah poin : 41.14
        Nilai Minimum : 5.0
        Quartil 1 (Q1) : 16.0
        Median (Q2): 25.0
        Quartil 3 (Q3) : 43.0
        Nilai Maksimum : 3300.0
        Standar Deviasi : 41.02

        Statistik Deskriptif price untuk negara Italy
        Rata-rata jumlah poin : 39.66
        Nilai Minimum : 5.0
        Quartil 1 (Q1) : 18.0
        Median (Q2): 28.0
        Quartil 3 (Q3) : 50.0
        Nilai Maksimum : 900.0
        Standar Deviasi : 41.02
        """

        similarity = find_string_similarity(self.statistical_descriptive.strip(),test_string.strip())
        try:
            assert similarity >= 0.75
            print(f'Similarity statistika descriptive = {similarity} >= 0.75')
            self.correct_ans+=1
        except AssertionError as e:
            print(e)
            print(f'Similarity statistika descriptive = {similarity} < 0.75')
            print("Statistical Descriptive Kurang Tepat!")
            self.wrong_ans+=1

    def run_all_tests(self):
        self.df_shape_test()
        self.df_column_names_test()
        self.df_datatypes_test()
        self.df_empty_rows_test()
        self.df_null_columns_test()
        self.df_statistical_descriptive_test()

        total_tests = self.wrong_ans + self.correct_ans
        if self.wrong_ans == 0: print(f"Semua {total_tests} Test Case Terlewati! Selamat!")
        else:
            print(f"Jumlah test yang berhasil dilewati {self.correct_ans}/{total_tests}")

test = Test((row,col), wine_df_columns, wine_df_datatypes,columns_with_null_values,num_of_empty_datas,statistika_deskriptif_string)
test.run_all_tests()