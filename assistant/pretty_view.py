from prettytable import PrettyTable


class BeautyView:
    def create_table(self, data):
        raise NotImplementedError

    def create_row(self, data):
        raise NotImplementedError


class AddressbookView(BeautyView):
    def create_table(self, data):
        x = PrettyTable()
        x.field_names = ['Name', 'Birthday', 'Email', 'Address', 'Phones']
        for i in data:
            x.add_row(i)
        return x

    def create_row(self, data):
        x = PrettyTable()
        x.field_names = ['Name', 'Birthday', 'Email', 'Address', 'Phones']
        x.add_row(data)
        return x


class NotebookView(BeautyView):
    def create_table(self, data):
        x = PrettyTable()
        x.field_names = ['Index', 'Tags', 'Note']
        for i in data:
            x.add_row(i)
        return x

    def create_row(self, data):
        x = PrettyTable()
        x.field_names = ['Index', 'Tags', 'Note']
        x.add_row(data)
        return x


class SortDirView(BeautyView):
    def create_row(self, data):
        x = PrettyTable()
        x.field_names = ['Known_extensions', "Unknown_extensions"]
        x.add_row(data)
        return x

    def create_table(self, data):
        pass