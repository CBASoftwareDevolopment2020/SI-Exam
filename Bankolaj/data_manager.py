import sqlite3
from sqlite3 import Error, Connection
from pprint import pprint as pp


def create_connection(db_file: str) -> Connection:
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


class DataManager:
    def __init__(self, db_file: str):
        self._conn: Connection = None
        self.get_connection(db_file)

    def get_connection(self, db_file: str) -> Connection:
        if self._conn is None:
            print('No connection set\nCreating connection')
            self._conn = create_connection(db_file)
        return self._conn

    def new_account(self, owner, acc_num, card_num, cvc):
        cur = self._conn.cursor()
        cur.execute('BEGIN')
        try:
            cur.execute(f"INSERT INTO accounts (accNum,owner) VALUES ('{acc_num}','{owner}');")
            cur.execute(f"INSERT INTO cards (cardNum,cvc,accId) VALUES ('{card_num}','{cvc}','{cur.lastrowid}');")
        except Error as e:
            print(e)
            cur.execute('ROLLBACK')
        finally:
            cur.execute('END')

    def setup_tables(self):
        drop_tables = '''   DROP TABLE IF EXISTS cards;
                            DROP TABLE IF EXISTS accounts;'''
        account_table = ''' CREATE TABLE accounts(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                accNum NCHAR(10) UNIQUE NOT NULL ,
                                balance INTEGER NOT NULL DEFAULT 0,
                                owner NVARCHAR(64) NOT NULL
                            )'''
        card_table = '''CREATE TABLE cards(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cardNum NCHAR(16) UNIQUE NOT NULL,
                            cvc NCHAR(3) NOT NULL,
                            accId INTEGER NOT NULL,
                            FOREIGN KEY (accId) REFERENCES accounts (id)
                        )'''
        try:
            print('Creating tables')
            self._conn.executescript(';\n'.join([drop_tables, account_table, card_table]))
            print('Tables created')
        except Error as e:
            print(e)

        self.populate_tables()

    def populate_tables(self):
        data = [('Michael Filipovic', '6331235806', '5019123400912666', '687', 0),
                ('Michael Filipovic', '6331235893', '5019123400912749', '421', 0),
                ('Michael Filipovic', '6331235900', '5019123400912831', '237', 0),
                ('Jonas Frehr', '6331235947', '5019123400912885', '009', 0),
                ('Jonas Lundsgaard', '6331236002', '5413123400912985', '103', 0),
                ('Christian Sabet', '6331236066', '4571123400913021', '021', 0),
                ('Christian Sabet', '6331236131', '5019123400913080', '163', 0),
                ('Christian Sabet', '6331236193', '5019123400913126', '714', 0),
                ('Alex Lindholm', '6331236231', '5413123400913211', '678', 0),
                ('Alex Lindholm', '6331236325', '5413123400913221', '763', 0),
                ('Jonatan Filipovic', '6331236406', '5019123400913296', '272', 0),
                ('Jonatan Filipovic', '6331236459', '4571123400913316', '521', 0),
                ('Daniel Højgaard', '6331236559', '4571123400913404', '428', 0),
                ('Daniel Højgaard', '6331236639', '5019123400913503', '242', 0),
                ('Daniel Højgaard', '6331236653', '5413123400913567', '095', 0),
                ('Jesper Andersen', '6331236709', '5019123400913641', '616', 0),
                ('Michael Vestergaard', '6331236727', '5019123400913705', '673', 0),
                ('Michael Vestergaard', '6331236770', '5413123400913734', '113', 0),
                ('Michael Vestergaard', '6331236848', '5413123400913762', '188', 0),
                ('Mohammad Sabet', '6331236931', '5413123400913834', '203', 0),
                ('Mohammad Sabet', '6331236935', '4571123400913914', '000', 0),
                ('Mohammad Sabet', '6331236946', '5019123400913995', '763', 0),
                ('Mathias Harvej', '6331236958', '4571123400914058', '305', 0),
                ('Mathias Harvej', '6331237019', '5019123400914118', '419', 0),
                ('Mathias Harvej', '6331237083', '5019123400914167', '347', 0),
                ('Jacob Kristensen', '6331237108', '4571123400914247', '119', 0),
                ('Jacob Kristensen', '6331237130', '5413123400914252', '558', 0),
                ('Joseph Rusbjerg', '6331237219', '5019123400914322', '258', 0),
                ('Joseph Rusbjerg', '6331237255', '5413123400914358', '086', 0),
                ('Joseph Rusbjerg', '6331237324', '5413123400914451', '358', 0),
                ('Mads Bakke', '6331237331', '5413123400914465', '215', 0),
                ('Mads Bakke', '6331237363', '4571123400914538', '607', 0),
                ('Benjamin Lundsgaard-Larsen', '6331237373', '5019123400914586', '930', 0),
                ('Benjamin Lundsgaard-Larsen', '6331237415', '4571123400914613', '349', 0),
                ('Mathias Højgaard', '6331237417', '5019123400914708', '680', 0),
                ('Mathias Højgaard', '6331237511', '4571123400914756', '754', 0),
                ('Kristoffer Jørgensen', '6331237563', '4571123400914817', '931', 0),
                ('Kristoffer Jørgensen', '6331237603', '4571123400914891', '247', 0),
                ('Christian Dimitrova', '6331237649', '5413123400914958', '449', 0),
                ('Martin Kristensen', '6331237709', '5019123400915053', '737', 0),
                ('Martin Kristensen', '6331237773', '5019123400915064', '322', 0),
                ('Martin Kristensen', '6331237807', '4571123400915126', '916', 0),
                ('Michael Jacobsen', '6331237877', '5019123400915183', '541', 0),
                ('Sebastian Togrou', '6331237925', '5019123400915240', '245', 0),
                ('Kimon Lindholm', '6331237985', '5413123400915290', '568', 0),
                ('Kimon Lindholm', '6331237991', '5019123400915301', '332', 0),
                ('Kimon Lindholm', '6331238090', '4571123400915350', '250', 0),
                ('Magnus Filipovic', '6331238132', '4571123400915433', '637', 0),
                ('Magnus Filipovic', '6331238187', '5413123400915469', '841', 0),
                ('Magnus Filipovic', '6331238211', '4571123400915485', '738', 0),
                ('Emil Bakke', '6331238275', '5413123400915582', '616', 0),
                ('Kimon Vestergaard', '6331238285', '4571123400915620', '594', 0),
                ('Andreas Rusbjerg', '6331238286', '5019123400915704', '405', 0),
                ('Andreas Rusbjerg', '6331238360', '4571123400915800', '006', 0),
                ('Nikolai Rusbjerg', '6331238411', '5019123400915835', '982', 0),
                ('Nikolai Rusbjerg', '6331238494', '5413123400915857', '769', 0),
                ('Nikolaj Grønbek', '6331238517', '5413123400915956', '297', 0),
                ('Jesper Saidane', '6331238566', '4571123400916022', '115', 0),
                ('Mathias Oertel', '6331238615', '4571123400916064', '924', 0),
                ('Mathias Oertel', '6331238618', '4571123400916133', '660', 0),
                ('Mathias Oertel', '6331238620', '4571123400916144', '672', 0),
                ('Thomas Djurhuus', '6331238691', '5413123400916172', '814', 0),
                ('Thomas Djurhuus', '6331238757', '5413123400916233', '032', 0),
                ('Christian Lindholm', '6331238842', '5019123400916290', '268', 0),
                ('Christian Lindholm', '6331238930', '4571123400916337', '742', 0),
                ('Magnus Borg', '6331239020', '4571123400916435', '856', 0),
                ('Magnus Borg', '6331239028', '4571123400916481', '869', 0),
                ('Mads Klitmose', '6331239042', '5019123400916518', '843', 0),
                ('Michael Sabet', '6331239043', '5413123400916545', '029', 0),
                ('Michael Sabet', '6331239135', '5019123400916564', '438', 0),
                ('Michael Sabet', '6331239183', '5019123400916604', '555', 0),
                ('Pernille Friis', '6331239206', '5413123400916652', '936', 0),
                ('Pernille Friis', '6331239230', '5413123400916699', '620', 0),
                ('Pernille Friis', '6331239301', '4571123400916793', '279', 0),
                ('Martin Djurhuus', '6331239313', '5413123400916853', '977', 0),
                ('Mohammad Feldt', '6331239380', '5413123400916881', '292', 0),
                ('Rasmus Lundsgaard', '6331239452', '5413123400916886', '914', 0),
                ('Rasmus Lundsgaard', '6331239527', '5413123400916927', '149', 0),
                ('Kenneth Langhoff', '6331239545', '5019123400916935', '302', 0),
                ('Kenneth Langhoff', '6331239641', '5019123400916942', '604', 0),
                ('Malene Hariri', '6331239684', '5019123400917024', '371', 0),
                ('Jonas Lindholm', '6331239744', '5413123400917053', '967', 0),
                ('Jonas Lindholm', '6331239842', '5413123400917153', '992', 0),
                ('Jesper Filipovic', '6331239860', '5019123400917219', '162', 0),
                ('Jesper Filipovic', '6331239928', '4571123400917273', '909', 0),
                ('Jesper Filipovic', '6331240011', '5019123400917369', '109', 0),
                ('Rasmus Pedersen', '6331240104', '4571123400917406', '981', 0),
                ('Rasmus Pedersen', '6331240153', '5413123400917435', '739', 0),
                ('Michael Dean', '6331240155', '4571123400917486', '181', 0),
                ('Michael Dean', '6331240184', '4571123400917568', '390', 0),
                ('Kristoffer Ebsen', '6331240228', '5413123400917572', '870', 0),
                ('Kristoffer Ebsen', '6331240248', '5413123400917611', '016', 0),
                ('Kristoffer Helsgaun', '6331240334', '4571123400917615', '270', 0),
                ('Kristoffer Helsgaun', '6331240406', '5413123400917628', '877', 0),
                ('Kristoffer Helsgaun', '6331240434', '5019123400917642', '270', 0),
                ('Pernille Højgaard', '6331240457', '5413123400917715', '786', 0),
                ('Thomas Rasmussen', '6331240459', '4571123400917815', '741', 0),
                ('Thomas Rasmussen', '6331240508', '5019123400917850', '723', 0),
                ('Mads Rasmussen', '6331240597', '5413123400917880', '849', 0),
                ('Mads Lass', '6331240678', '4571123400917972', '042', 0),
                ('Mads Lass', '6331240724', '5413123400918070', '074', 0),
                ('Mads Lass', '6331240769', '4571123400918089', '398', 0),
                ('Emil Lundsgaard-Larsen', '6331240853', '5019123400918138', '390', 0),
                ('Emil Lundsgaard-Larsen', '6331240870', '5019123400918176', '384', 0),
                ('Emil Lundsgaard-Larsen', '6331240947', '4571123400918272', '123', 0),
                ('Tobias Heick', '6331241036', '5413123400918275', '751', 0),
                ('Malene Borg', '6331241061', '5413123400918331', '738', 0),
                ('Malene Borg', '6331241068', '5019123400918406', '358', 0),
                ('Malene Borg', '6331241155', '5019123400918459', '038', 0),
                ('Nur-Alhussein Togrou', '6331241171', '5019123400918485', '214', 0),
                ('Emil Friis', '6331241183', '5413123400918490', '972', 0),
                ('Todorka Moustesgård', '6331241246', '5019123400918514', '035', 0),
                ('Todorka Frehr', '6331241299', '5413123400918515', '044', 0),
                ('Todorka Frehr', '6331241391', '4571123400918599', '825', 0),
                ('Todorka Frehr', '6331241469', '5413123400918686', '263', 0),
                ('Rasmus Lørup', '6331241499', '5413123400918696', '708', 0),
                ('Rasmus Lørup', '6331241501', '4571123400918793', '907', 0),
                ('Daniel Sabet', '6331241576', '4571123400918862', '467', 0),
                ('Daniel Sabet', '6331241605', '5019123400918869', '728', 0),
                ('Daniel Sabet', '6331241704', '5019123400918913', '201', 0),
                ('Michael Bojesen', '6331241764', '5413123400919010', '184', 0),
                ('Morten Dean', '6331241823', '5413123400919062', '211', 0),
                ('Morten Dean', '6331241860', '5413123400919124', '857', 0),
                ('Joseph Jacobsen', '6331241953', '5413123400919198', '348', 0),
                ('Joseph Jacobsen', '6331241982', '5413123400919218', '182', 0),
                ('Tobias Langhoff', '6331242045', '4571123400919220', '088', 0),
                ('Tobias Langhoff', '6331242050', '5413123400919229', '543', 0),
                ('Nikolaj Højgaard', '6331242078', '4571123400919264', '455', 0),
                ('Nikolaj Højgaard', '6331242157', '5413123400919321', '905', 0),
                ('Kristoffer Hein', '6331242166', '4571123400919371', '847', 0),
                ('Kristoffer Hein', '6331242176', '4571123400919460', '494', 0),
                ('Jörg Lindholm', '6331242179', '5413123400919519', '405', 0),
                ('Jacob Rusbjerg', '6331242246', '4571123400919564', '036', 0),
                ('Kimon Kramath', '6331242288', '4571123400919599', '285', 0),
                ('Kimon Kramath', '6331242366', '4571123400919647', '844', 0),
                ('Jesper Borg', '6331242378', '5019123400919704', '334', 0),
                ('Jesper Borg', '6331242393', '5413123400919797', '120', 0),
                ('Jesper Borg', '6331242460', '5413123400919861', '370', 0),
                ('Mohammad Vestergaard', '6331242500', '4571123400919864', '834', 0),
                ('Mohammad Vestergaard', '6331242571', '5413123400919882', '843', 0),
                ('Alex Ebsen', '6331242591', '4571123400919956', '040', 0),
                ('Alex Ebsen', '6331242661', '5413123400919993', '429', 0),
                ('Alex Ebsen', '6331242667', '4571123400920079', '123', 0),
                ('Benjamin Borg', '6331242703', '5019123400920177', '842', 0),
                ('Pernille Langhoff', '6331242798', '5019123400920239', '509', 0),
                ('Pernille Langhoff', '6331242819', '5413123400920243', '689', 0),
                ('Pernille Langhoff', '6331242854', '5413123400920279', '456', 0),
                ('Jesper Togrou', '6331242870', '5413123400920293', '121', 0),
                ('Jesper Togrou', '6331242884', '4571123400920310', '672', 0),
                ('Jesper Togrou', '6331242983', '4571123400920341', '275', 0),
                ('Jacob Togrou', '6331243019', '4571123400920380', '544', 0),
                ('Jacob Togrou', '6331243036', '5019123400920410', '370', 0),
                ('Adam Djurhuus', '6331243091', '5413123400920454', '130', 0),
                ('Adam Djurhuus', '6331243094', '5019123400920537', '365', 0),
                ('Adam Djurhuus', '6331243098', '5413123400920603', '826', 0),
                ('Benjamin Dimitrova', '6331243117', '5019123400920670', '291', 0),
                ('Todorka Rasmussen', '6331243125', '4571123400920709', '177', 0),
                ('Todorka Rasmussen', '6331243161', '4571123400920798', '750', 0),
                ('Todorka Rasmussen', '6331243210', '5413123400920889', '197', 0),
                ('Pernille Sabet', '6331243222', '5413123400920897', '964', 0),
                ('Jonatan Sabet', '6331243287', '4571123400920955', '123', 0),
                ('Martin Lass', '6331243355', '5413123400921047', '590', 0),
                ('Jörg Jacobsen', '6331243361', '5019123400921062', '815', 0),
                ('Jörg Jacobsen', '6331243455', '5413123400921160', '370', 0),
                ('Jörg Jacobsen', '6331243479', '4571123400921211', '868', 0),
                ('Kenneth Jørgensen', '6331243558', '5413123400921235', '199', 0),
                ('Kenneth Jørgensen', '6331243609', '5019123400921241', '015', 0),
                ('Anders Heick', '6331243610', '5019123400921308', '353', 0),
                ('Anders Heick', '6331243663', '4571123400921333', '245', 0),
                ('Andreas Hermansen', '6331243752', '5413123400921365', '240', 0),
                ('Andreas Hermansen', '6331243759', '5019123400921394', '033', 0),
                ('Andreas Hermansen', '6331243816', '5019123400921446', '170', 0),
                ('Andreas Dimitrova', '6331243818', '4571123400921477', '435', 0),
                ('Andreas Dimitrova', '6331243872', '4571123400921514', '806', 0),
                ('Benjamin Klitmose', '6331243877', '5019123400921520', '547', 0),
                ('Joseph Rasmussen', '6331243969', '4571123400921607', '663', 0),
                ('Joseph Rasmussen', '6331243971', '5413123400921628', '576', 0),
                ('Joseph Rasmussen', '6331244043', '4571123400921648', '972', 0),
                ('Mohammad Lindholm', '6331244103', '4571123400921726', '725', 0),
                ('Mathias Filipovic', '6331244187', '5413123400921789', '329', 0),
                ('Mathias Filipovic', '6331244233', '5413123400921841', '995', 0),
                ('Magnus Langhoff', '6331244263', '4571123400921937', '347', 0),
                ('Christian Hein', '6331244321', '5019123400921941', '227', 0),
                ('Christian Hein', '6331244370', '5019123400922027', '369', 0),
                ('Christian Hein', '6331244372', '4571123400922061', '647', 0),
                ('Adam Filipovic', '6331244456', '5413123400922106', '686', 0),
                ('Nur-Alhussein Lindholm', '6331244521', '5019123400922172', '127', 0),
                ('Nur-Alhussein Lindholm', '6331244562', '4571123400922216', '355', 0),
                ('Mohammad Langhoff', '6331244656', '5413123400922262', '693', 0),
                ('Mohammad Langhoff', '6331244742', '4571123400922357', '078', 0),
                ('Mohammad Langhoff', '6331244782', '5413123400922438', '416', 0),
                ('Adam Saidane', '6331244869', '5413123400922528', '075', 0),
                ('Adam Saidane', '6331244893', '5019123400922617', '882', 0)]

        for item in data:
            owner, acc_num, card_num, cvc, _ = item
            self.new_account(owner, acc_num, card_num, cvc)

    def print_tables(self):
        cursor = self._conn.cursor()
        try:
            cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
        except Error as e:
            print(e)
        pp(cursor.fetchall())

    def print_data(self):
        cursor = self._conn.cursor()
        try:
            cursor.execute("""  SELECT accounts.owner,accounts.accNum,cards.cardNum,cards.cvc,accounts.balance
                                FROM cards
                                JOIN accounts
                                    WHERE cards.accId = accounts.id""")
        except Error as e:
            print(e)
        pp(cursor.fetchall())

    def update_balance(self, acc_num: str, amt: int) -> bool:
        cur = self._conn.cursor()
        try:
            cur.execute("SELECT * FROM accounts WHERE accNum = ?", (acc_num,))
            acc_id, _, balance, owner = cur.fetchone()
            cur.execute("UPDATE accounts SET balance = ? WHERE id = ?", (balance + amt, acc_id))
            if cur.rowcount < 1:
                return False
            else:
                return True
        except Error as e:
            print(e)

    def validate_card(self, card_num: str, cvc: str) -> bool:
        cur = self._conn.cursor()
        try:
            cur.execute("SELECT * FROM cards WHERE cardNum = ? AND cvc = ?", (card_num, cvc))
            res = cur.fetchone()
            if res:
                return True
            return False
        except Error as e:
            print(e)

    def validate_account(self, acc_num: str) -> bool:
        cur = self._conn.cursor()
        try:
            cur.execute("SELECT * FROM accounts WHERE accNum = ?", (acc_num,))
            res = cur.fetchone()
            if res:
                return True
            return False
        except Error as e:
            print(e)


if __name__ == '__main__':
    dm = DataManager(r"db\bankolaj.db")
