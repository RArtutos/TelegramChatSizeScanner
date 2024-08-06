from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel, Message
from tqdm import tqdm
import config
import asyncio

# Inicializa el cliente de Telethon
client = TelegramClient('session_name', config.api_id, config.api_hash)

def format_size(size_bytes):
    """Convierte el tamaño en bytes a una representación legible (KB, MB, GB, TB)."""
    if size_bytes < 1024:
        return f"{size_bytes:.2f} Bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    elif size_bytes < 1024 * 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"
    elif size_bytes < 1024 * 1024 * 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024 * 1024 * 1024):.2f} TB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024 * 1024 * 1024):.2f} PB"

async def main():
    await client.start(phone=config.phone_number)
    
    # Obtén la entidad del chat usando chat_id desde config.py
    channel = await client.get_entity(config.chat_id)
    
    # Inicializa variables para el cálculo de tamaños
    total_characters = 0
    total_files_size_bytes = 0
    total_messages = 0

    # Define la velocidad de las peticiones (en segundos)
    speed = 2  # Retraso entre peticiones, ajustar según sea necesario
    
    # Obtén el historial de mensajes
    history = await client(GetHistoryRequest(
        peer=channel,
        offset_id=0,
        offset_date=None,
        add_offset=0,
        limit=100,
        max_id=0,
        min_id=0,
        hash=0
    ))
    
    total_messages = history.count
    print(f'Total messages to scan: {total_messages}')
    
    # Usa tqdm para la barra de progreso
    with tqdm(total=total_messages, unit='message') as pbar:
        offset_id = 0
        
        while True:
            history = await client(GetHistoryRequest(
                peer=channel,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=100,
                max_id=0,
                min_id=0,
                hash=0
            ))
            
            if not history.messages:
                break
            
            for message in history.messages:
                if isinstance(message, Message):
                    if message.message:
                        # Calcular tamaño del mensaje en bytes
                        message_size_bytes = len(message.message.encode('utf-8'))
                        total_characters += len(message.message)
                        total_files_size_bytes += message_size_bytes
                    
                    if message.media and hasattr(message.media, 'document'):
                        # Calcular tamaño del archivo
                        total_files_size_bytes += message.media.document.size

                # Actualiza la barra de progreso
                pbar.set_postfix({
                    'Characters': f"{total_characters:,}",
                    'Files Size': format_size(total_files_size_bytes)
                })
                pbar.update(1)
            
            offset_id = history.messages[-1].id
            
            # Retraso entre peticiones para evitar superar los límites
            await asyncio.sleep(speed)

    # Imprime los resultados finales en un formato adecuado
    print(f'\nTotal characters: {total_characters:,}')
    print(f'Total size of files: {format_size(total_files_size_bytes)}')

# Ejecuta el cliente de Telethon
with client:
    client.loop.run_until_complete(main())
