from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.inode import Inode
from ...types import Response


def _get_kwargs(
    mnemonic: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/fs/{mnemonic}/duplicate",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Inode]:
    if response.status_code == 200:
        response_200 = Inode.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Inode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mnemonic: str,
    *,
    client: AuthenticatedClient,
) -> Response[Inode]:
    """
    Args:
        mnemonic (str): mnemonics are human readable unique identifiers for datasets
            mnemonics have the form <random adjective>_<random first name> Example: happy_jane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Inode]
    """

    kwargs = _get_kwargs(
        mnemonic=mnemonic,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mnemonic: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Inode]:
    """
    Args:
        mnemonic (str): mnemonics are human readable unique identifiers for datasets
            mnemonics have the form <random adjective>_<random first name> Example: happy_jane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Inode
    """

    return sync_detailed(
        mnemonic=mnemonic,
        client=client,
    ).parsed


async def asyncio_detailed(
    mnemonic: str,
    *,
    client: AuthenticatedClient,
) -> Response[Inode]:
    """
    Args:
        mnemonic (str): mnemonics are human readable unique identifiers for datasets
            mnemonics have the form <random adjective>_<random first name> Example: happy_jane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Inode]
    """

    kwargs = _get_kwargs(
        mnemonic=mnemonic,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mnemonic: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Inode]:
    """
    Args:
        mnemonic (str): mnemonics are human readable unique identifiers for datasets
            mnemonics have the form <random adjective>_<random first name> Example: happy_jane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Inode
    """

    return (
        await asyncio_detailed(
            mnemonic=mnemonic,
            client=client,
        )
    ).parsed
