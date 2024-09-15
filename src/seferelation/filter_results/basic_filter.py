ADDRESS_OF_SEFARIA = "https://www.sefaria.org.il/"


class Filter:
    def __init__(self):
        pass



    def link2path(self, link):
        if not link[0:len(ADDRESS_OF_SEFARIA)] == ADDRESS_OF_SEFARIA:
            raise Exception('the link is broken')
        return link[len(ADDRESS_OF_SEFARIA):]

    def path2link(self, path):
        return ADDRESS_OF_SEFARIA + path

    def Do_it_close(self, link1, link2):
        path1, path2 = self.link2path(link1), self.link2path(link2)
        path1_lst = path1.split('.')
        path2_lst = path2.split('.')
        flag = False        # this flag is true if the links id closed.

        # now we will use checks to decide the value of flag.
        # the checks is with 'or' operator between them.

        # almost same place (same chapter)
        if path1_lst[:-1] == path2_lst[:-1]:
            flag = True


        # pirush on test:
        if ('_on_' in path1_lst[0]) and (path2_lst[0] == path1_lst[0].split('_on_')[1]) and (path1_lst[1:-1] == path2_lst[1:])\
                or \
           ('_on_' in path2_lst[0]) and (path1_lst[0] == path2_lst[0].split('_on_')[1]) and (path1_lst[1:] == path2_lst[1:-1]):
            flag = True

        return flag
