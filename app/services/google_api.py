from datetime import datetime
from typing import List

from aiogoogle import Aiogoogle

from app.core.config import settings


FORMAT = "%Y/%m/%d %H:%M:%S"
VERSION_SHEETS = 'v4'
VERSION_DRIVE = 'v3'
SHEET_ID = 0
TITLE_CLOSE_SPEED = 'Скорость закрытия'
ROW_COUNT = 100
COLUMN_COUNT = 11
LOCALE = 'ru_RU'


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover('sheets', VERSION_SHEETS)
    spreadsheets_body = {
        'properties': {'title': f'QRKot_Отчет от {datetime.now().strftime(FORMAT)}',
                       'locale': LOCALE},
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': SHEET_ID,
                'title': TITLE_CLOSE_SPEED,
                'gridProperties': {
                    'rowCount': ROW_COUNT,
                    'columnCount': COLUMN_COUNT
                }
            }
        }]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheets_body)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


async def set_user_permissions(
    spreadsheetid: str,
    wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', VERSION_DRIVE)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields='id'
        )
    )


async def spreadsheets_update_value(
    spreadsheetid: str,
    projects: List,
    wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('sheets', VERSION_SHEETS)
    table_values = [
        ['Отчет от', datetime.now().strftime(FORMAT)],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    for project in projects:
        new_row = [
            str(project['name']),
            str(project['duration']),
            str(project['description'])
        ]
        table_values.append(new_row)
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    all_lines = len(table_values)
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=f'A1:C{all_lines}',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )